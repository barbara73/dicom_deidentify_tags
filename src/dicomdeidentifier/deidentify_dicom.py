"""
Deidentifier:

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
from pydicom.uid import generate_uid
from pydicom import FileDataset
from pydicom.dataset import Dataset
from logdecoratorandhandler.log_decorator import LogDecorator

from .rule_sets import timeshift_custom_ruleset, no_times_ruleset


class NoTimeShiftError(Exception):
    pass


class NoDatesElementFoundError(Exception):
    pass


@LogDecorator('INFO - remove pixel data')
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


@dataclass
class DeidentifyDataset:
    """
    Deidentifier for de-identifying dicom content with basic profile
    and custom dates and UIDs.
    """
    lookup: LookupID

    @staticmethod
    @LogDecorator('INFO - get date elements')
    def get_date_elements(ds: Dataset) -> dict:
        """
        Get all the date data elements of not de-identified dates and make dictionary.
        :return:
        """
        try:
            return {de: ds.data_element(de).value for de in ds.dir('date')}
        except TypeError:
            return {}

    @LogDecorator('INFO - deidentify dates')
    def deidentify_dates(self, ds: Dataset) -> Dataset:
        """
        Deidentify the dates from dictionary which collected all the dates in data elements.

        Since you can remove dates entirely (custom rule sets), handle with key error.
        If you do not have a time shift, then you get a type error.
        If you have different date time formats, you will get a value error.

        Need to set PatientBirthDate explicitely to None if not removed in rule set.
        :param ds:      A pydicom dataset with date and datetime tags
                        (already changed/deidentified in a first step)
        :return:        modified dataset (date shift)
        """
        shift = self.lookup.time_shift

        for element, date in self.get_date_elements(ds).items():
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
                        new_time = datetime.strptime(date, '%Y%m%d%H%M%S') + timedelta(days=shift)
                        ds.data_element(element).value = new_time.strftime('%Y%m%d%H%M%S')
                    else:
                        ds.data_element(element).value = None

        return ds

    @LogDecorator("INFO - add de-identified uid's")
    def add_deid_uids(self, ds: Dataset) -> Dataset:
        """
        Add our UIds to deidentified data elements.
        """
        if self.lookup.deid_patient_id is None:
            ds.PatientID = str(uuid)
        else:
            ds.PatientID = self.lookup.deid_patient_id

        if self.lookup.deid_study_uid is None:
            ds.StudyInstanceUID = str(generate_uid(prefix=None))
        else:
            ds.StudyInstanceUID = self.lookup.deid_study_uid

        if self.lookup.deid_series_uid is None:
            ds.SeriesInstanceUID = str(generate_uid(prefix=None))
        else:
            ds.SeriesInstanceUID = self.lookup.deid_series_uid

        ds.SOPInstanceUID = str(generate_uid(prefix=None))
        self.lookup.deid_sop_uid = ds.SOPInstanceUID
        ds.file_meta.MediaStorageSOPClassUID = ds.SOPInstanceUID
        return ds

    @LogDecorator('INFO - get de-identified data set')
    def get_deid_dataset(self, ds: Dataset) -> tuple:
        """
        Deidentify dicom content with specific rules.
        Add rule sets if needed in the rule_sets.
        Timedelta could be set directly in rule set - not done this way - check.
        Later rules overrule previous.
        """
        deid_content = self.add_deid_uids(ds)            # added deidentified uids to ds

        if self.lookup.time_shift in (0, None):
            profile = Profile(
                rule_sets=[timeshift_custom_ruleset,
                           no_times_ruleset,            # delete all times
                           ])
        else:
            profile = Profile(
                rule_sets=[timeshift_custom_ruleset,
                           ])

        core = Core(profile=profile,            # Create an deidentification core
                    pixel_processor=None        # here you would add the pixel location
                    )
        try:
            # deidentification with rule set
            deid_content = core.deidentify(deid_content)
        except AttributeError:
            pass

        deid_content = self.deidentify_dates(deid_content)       # deidentified dates (not times)

        return FileDataset(self.lookup.filename,
                           deid_content,
                           ds.preamble,
                           ds.file_meta,
                           ds.read_implicit_vr,
                           ds.read_little_endian
                           ), self.lookup
