"""
De-identifier:

- remove pixel data
(can be chosen for export with remove_pixel_data=True in config.ini)

if deidentify=True in config.ini then:
- time shift
- basic rules
- add generated UIDs
"""
import uuid
from dataclasses import dataclass, field
from datetime import datetime, timedelta
from typing import Optional
from idiscore.core import Core, Profile
from pydicom.uid import generate_uid, validate_value
from pydicom import FileDataset, Sequence
from pydicom.dataset import Dataset

from .rule_sets import timeshift_custom_ruleset, no_times_ruleset


class NoTimeShiftError(Exception):
    pass


class NoDatesElementFoundError(Exception):
    pass


def remove_pixel_data(content: Dataset) -> str:
    """
    Remove pixel data for export with DB. Not yet implemented.
    """
    if hasattr(content, 'PixelData'):
        del content.PixelData

    return content.to_json()


@dataclass
class LookupID:
    """Look-up for de-identified uid's."""
    filename: Optional[str] = field(default=None)
    deid_patient_id: Optional[str] = field(default=None)
    deid_study_uid: Optional[str] = field(default=None)
    deid_series_uid: Optional[str] = field(default=None)
    deid_sop_uid: Optional[str] = field(default=None)
    time_shift: Optional[int] = field(default=None)
    private_tags: bool = field(default=False)


@dataclass
class DeidentifyDataset:
    """
    De-identifier for de-identifying dicom content with basic profile
    and custom dates and UIDs.
    """
    lookup: LookupID

    @staticmethod
    def get_date_elements(ds: Dataset) -> dict:
        """
        Get all the date data elements of not de-identified dates and make dictionary.
        :return:
        """
        try:
            return {de: ds.data_element(de).value for de in ds.dir('date')}
        except TypeError:
            return {}

    def deidentify_dates(self, ds: Dataset) -> Dataset:
        """
        Deidentify the dates from dictionary which collected all the dates in data elements.

        Since you can remove dates entirely (custom rule sets), handle with key error.
        If you do not have a time shift, then you get a type error.
        If you have different date time formats, you will get a value error.

        Need to set PatientBirthDate explicitly to None if not removed in rule set.
        Args:
        :param ds:      A pydicom dataset with date and datetime tags
                        (already changed/de-identified in a first step)
        :return:        modified dataset (date shift)
        """
        shift = self.lookup.time_shift

        for element, date in self.get_date_elements(ds).items():
            try:
                if shift in (0, None) or date is None:
                    ds.data_element(element).value = None
                else:
                    if element == 'PatientBirthDate':
                        ds.data_element(element).value = None
                    else:
                        if len(date) == 8:
                            new_time = datetime.strptime(date, '%Y%m%d') + timedelta(days=shift)
                            ds.data_element(element).value = new_time.strftime('%Y%m%d')
                        elif len(date.partition('.')[0]) == 14:
                            date = date.partition('.')[0]
                            new_time = datetime.strptime(date, '%Y%m%d%H%M%S') \
                                       + timedelta(days=shift)
                            ds.data_element(element).value = new_time.strftime('%Y%m%d%H%M%S')
                        else:
                            ds.data_element(element).value = None
            except TypeError:
                ds.data_element(element).value = None
        return ds

    def add_deid_uids(self, ds: Dataset) -> Dataset:
        """
        Add our UIds to de-identified data elements.
        """
        if self.lookup.deid_patient_id is None:
            ds.PatientID = str(uuid.uuid4())
        else:
            ds.PatientID = str(self.lookup.deid_patient_id)

        if self.lookup.deid_study_uid is None:
            ds.StudyInstanceUID = str(generate_uid(prefix=None))
        else:
            validate_value('UI', self.lookup.deid_study_uid, 2)
            ds.StudyInstanceUID = str(self.lookup.deid_study_uid)

        if self.lookup.deid_series_uid is None:
            ds.SeriesInstanceUID = str(generate_uid(prefix=None))
        else:
            validate_value('UI', self.lookup.deid_series_uid, 2)
            ds.SeriesInstanceUID = str(self.lookup.deid_series_uid)

        if self.lookup.deid_sop_uid is None:
            ds.SOPInstanceUID = str(generate_uid(prefix=None))
            self.lookup.deid_sop_uid = ds.SOPInstanceUID
        else:
            validate_value('UI', self.lookup.deid_sop_uid, 2)
            ds.SOPInstanceUID = str(self.lookup.deid_sop_uid)

        ds.file_meta.MediaStorageSOPInstanceUID = ds.SOPInstanceUID
        return ds

    def get_deid_dataset(self, ds: Dataset) -> tuple:
        """
        Deidentify dicom content with specific rules.
        Add rule sets if needed in the rule_sets.
        Timedelta could be set directly in rule set - not done this way - check.
        Later rules overrule previous.

        Add information to tags, that the patient identity is removed and with what method.
        """
        if self.lookup.time_shift in (0, None):
            profile = Profile(
                rule_sets=[timeshift_custom_ruleset,
                           no_times_ruleset,  # delete all times
                           ])
            ds_1 = Dataset()
        else:
            profile = Profile(
                rule_sets=[timeshift_custom_ruleset,
                           ])
            ds_1 = Dataset()
            ds_1.CodeValue = '113107'

        core = Core(profile=profile,        # Create an de-identification core
                    pixel_processor=None    # here you would add the pixel location
                    )

        deid_content = self.add_deid_uids(ds)  # added de-identified uids to ds

        try:
            # de-identification with rule set
            deid_content = core.deidentify(deid_content)
        except AttributeError:
            pass
        except ValueError:
            pass

        deid_content = self.deidentify_dates(deid_content)  # de-identified dates (not times)
        x = deid_content

        # remove private tags, because they could have identity information
        deid_content.remove_private_tags()
        y = deid_content

        if x is not y:
            self.lookup.private_tags = True

        deid_content.PatientIdentityRemoved = 'YES'
        deid_content.DeidentificationMethod = '{Per DICOM PS 3.15 AnnexE. Details in 0012,0064}'

        ds_sq = Dataset()
        ds_sq.CodeValue = '113100'

        deid_content.DeidentificationMethodCodeSequence = Sequence([ds_sq, ds_1])

        return FileDataset(self.lookup.filename,
                           deid_content,
                           ds.preamble,
                           ds.file_meta,
                           ds.read_implicit_vr,
                           ds.read_little_endian
                           ), self.lookup
