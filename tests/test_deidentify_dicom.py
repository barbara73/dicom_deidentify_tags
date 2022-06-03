"""
Test Deidentify dicom data module
"""
import pytest
from pydicom import Dataset

from src.dicomdeidentifier.deidentify_dicom import DeidentifyDataset, LookupID
from tests.factories import quick_dataset


def test_can_get_date_elements(datetime_dataset):
    """Test can get date or datetime elements."""
    assert DeidentifyDataset.get_date_elements(
        datetime_dataset) == {'AcquisitionDate': '19800501',
                              'AcquisitionDateTime': '19800501163601',
                              'PatientBirthDate': '19800501',
                              'SeriesDate': '19730825121212.120000',
                              'StudyDate': '20190202'}


def test_date_elements_return_empty_dict(a_dataset):
    """Test returns empty dict if no date element."""
    assert DeidentifyDataset.get_date_elements(a_dataset) == {}


def test_deidentify_dates_dates_none_with_timeshift_none(datetime_dataset):
    """Test returns None if no time shift available."""
    lookup = LookupID()
    deid_ds = DeidentifyDataset(lookup).deidentify_dates(datetime_dataset)
    assert deid_ds.data_element('PatientBirthDate').value is None
    assert deid_ds.data_element('StudyDate').value is None
    assert deid_ds.SeriesDate is None
    assert deid_ds.AcquisitionDateTime is None
    assert deid_ds.AcquisitionTime is not None


def test_deidentify_dates_patient_birthdate_none_with_timeshift(datetime_dataset):
    """Test returns None for Patient Birth Date element (time shift not None)."""
    lookup = LookupID(time_shift=13)
    deid_ds = DeidentifyDataset(lookup).deidentify_dates(datetime_dataset)
    assert deid_ds.data_element('PatientBirthDate').value is None
    assert deid_ds.PatientBirthDate is None
    assert deid_ds.data_element('StudyDate').value is not None

    datetime_dataset.PatientBirthDate = "19730825121212.120000"
    deid_ds = DeidentifyDataset(lookup).deidentify_dates(datetime_dataset)
    assert deid_ds.PatientBirthDate is None


@pytest.mark.parametrize("ds", [quick_dataset(SeriesDate=""),
                                quick_dataset(SeriesDate=None),
                                ],
                         )
def test_deidentify_dates_where_date_none_with_timeshift(ds):
    """Test returns None if date is None or empty with time shift."""
    lookup = LookupID(time_shift=13)
    deid_ds = DeidentifyDataset(lookup).deidentify_dates(ds)
    assert deid_ds.SeriesDate is None


def test_deidentify_dates_with_positive_timeshift(datetime_dataset):
    """Test returns date element shifted by time shift."""
    lookup = LookupID(time_shift=16)
    deid_ds = DeidentifyDataset(lookup).deidentify_dates(datetime_dataset)
    assert deid_ds.data_element('SeriesDate').value == '19730910121212'
    assert deid_ds.StudyDate == '20190218'
    assert deid_ds.AcquisitionDateTime == '19800517163601'
    assert deid_ds.AcquisitionDate == '19800517'
    assert deid_ds.PatientBirthDate is None


def test_deidentify_dates_with_negative_timeshift(datetime_dataset):
    """Test deidentify dates without dateshift. Same string will be returned."""
    lookup = LookupID(time_shift=-30)
    deid_ds = DeidentifyDataset(lookup).deidentify_dates(datetime_dataset)
    assert deid_ds.data_element('SeriesDate').value == '19730726121212'
    assert deid_ds.StudyDate == '20190103'
    assert deid_ds.AcquisitionDateTime == '19800401163601'
    assert deid_ds.AcquisitionDate == '19800401'
    assert deid_ds.PatientBirthDate is None


@pytest.mark.parametrize("ds", [quick_dataset(SeriesDate="1973082", AcquisitionDateTime="19730825121212120000"),
                                quick_dataset(SeriesDate="197382", AcquisitionDateTime="1973085121212120000"),
                                quick_dataset(SeriesDate="19732", AcquisitionDateTime="197308512212120000"),
                                ],
                         )
def test_deidentify_dates_with_wrong_date_length(ds):
    """Test returns None if wrong date or datetime length."""
    lookup = LookupID(time_shift=30)
    deid_ds = DeidentifyDataset(lookup).deidentify_dates(ds)
    assert deid_ds.data_element('SeriesDate').value is None
    assert deid_ds.AcquisitionDateTime is None


def test_deidentify_dates_with_wrong_time_shift_type(datetime_dataset):
    """Test returns None if wrong date or datetime length."""
    lookup = LookupID(time_shift='e')
    deid_ds = DeidentifyDataset(lookup).deidentify_dates(datetime_dataset)
    assert deid_ds.data_element('SeriesDate').value is None
    assert deid_ds.AcquisitionDateTime is None


@pytest.mark.parametrize("ds",
                         [quick_dataset(SOPClassUID='1.2.840.10008.5.1.4.1.1.11.1',
                                        StudyInstanceUID='2.25.22070338010590029158579',
                                        SeriesInstanceUID='2.25.22070338010590029158579'),
                          quick_dataset(PatientID=1),
                          quick_dataset(SeriesDescription="Annotation"),
                          quick_dataset(SOPClassUID="1.2.840.10008.5.1.4.1.1.11.1",
                                        StudyInstanceUID="not_annotation"),
                          ],
                         )
def test_add_deid_uids(a_lookup, ds):
    """Test add deidentified uids are ok."""
    ds.file_meta = Dataset()
    ds.file_meta.MediaStorageSOPInstanceUID = 'a_UID'
    ds_uid = DeidentifyDataset(a_lookup).add_deid_uids(ds)
    assert ds_uid.PatientID == 'a_patient_id'
    assert ds_uid.StudyInstanceUID == '1.25.220703380105900291585793573'
    assert ds_uid.SeriesInstanceUID == '2.25.22070338010590029158579357354431'
    assert ds_uid.SOPInstanceUID != '1.2.840.10008.5.1.4.1.1.11.1'
    assert ds_uid.SOPInstanceUID == a_lookup.deid_sop_uid


@pytest.mark.parametrize("ds",
                         [quick_dataset(SOPClassUID="1.2.840.10008.5.1.4.1.1.11.1",
                                        StudyInstanceUID="1.2.33333333333",
                                        SeriesInstanceUID="1.3.44444444444"),
                          quick_dataset(PatientID=1),
                          quick_dataset(SeriesDescription="Annotation"),
                          quick_dataset(SOPClassUID="1.2.840.10008.5.1.4.1.1.11.1",
                                        StudyInstanceUID="not_annotation"),
                          ],
                         )
def test_add_deid_uids_with_wrong_types_throw_error(wrong_type_lookup, ds):
    """Test add deidentified uids are ok."""
    ds.file_meta = Dataset()
    ds.file_meta.MediaStorageSOPInstanceUID = 'a_UID'

    with pytest.raises(ValueError):
        DeidentifyDataset(wrong_type_lookup).add_deid_uids(ds)


@pytest.mark.parametrize("ds",
                         [quick_dataset(SOPClassUID="1.2.840.10008.5.1.4.1.1.11.1",
                                        StudyInstanceUID="1.2.33333333333",
                                        SeriesInstanceUID="1.3.44444444444"),
                          quick_dataset(PatientID=1),
                          quick_dataset(SeriesDescription="Annotation"),
                          quick_dataset(SOPClassUID="1.2.840.10008.5.1.4.1.1.11.1",
                                        StudyInstanceUID="not_annotation"),
                          ],
                         )
def test_add_deid_uids_if_no_lookup(ds):
    ds.file_meta = Dataset()
    ds.file_meta.MediaStorageSOPInstanceUID = 'a_UID'
    ds_uid = DeidentifyDataset().add_deid_uids(ds)
    assert ds_uid.PatientID is not None
    assert ds_uid.SOPInstanceUID is not None
    assert ds_uid.SeriesInstanceUID is not None
    assert ds_uid.StudyInstanceUID is not None


def test_get_deid_dataset_good(datetime_dataset, a_lookup):
    """Test get deidentified file data set."""
    datetime_dataset.file_meta = Dataset()
    datetime_dataset.preamble = 'b'
    datetime_dataset.file_meta.MediaStorageSOPInstanceUID = 'a_UID'
    file_ds, lookup = DeidentifyDataset(a_lookup).get_deid_dataset(datetime_dataset)
    assert lookup.deid_sop_uid is not None
    assert file_ds.file_meta.MediaStorageSOPClassUID is not None
    assert file_ds.SOPInstanceUID == lookup.deid_sop_uid
    assert file_ds.file_meta.MediaStorageSOPClassUID == lookup.deid_sop_uid
    assert file_ds.SeriesDate == '19730826121212'
    assert file_ds.AcquisitionTime == '163601'


@pytest.mark.parametrize("lookup", [LookupID(time_shift=0, filename='a_filename'),
                                    LookupID(time_shift=None, filename='a_filename')
                                    ],
                         )
def test_get_deid_dataset_no_timeshift(datetime_dataset, lookup):
    """Test set file data set deletes all times from data set."""
    datetime_dataset.file_meta = Dataset()
    datetime_dataset.preamble = 'b'
    file_ds, lookup = DeidentifyDataset(lookup).get_deid_dataset(datetime_dataset)
    assert file_ds.SeriesDate is None

    with pytest.raises(AttributeError):
        print(file_ds.AcquisitionTime)


def test_quick_dataset():
    test = quick_dataset(PatientID=123, PatientName="Jack", StudyDescription="Test")
    assert test.PatientID == 123
    assert test.PatientName == "Jack"
    assert test.StudyDescription == "Test"

    with pytest.raises(ValueError):
        quick_dataset(unknown_tag="shouldfail")


def test_set_new_data_element_by_name():
    """Dataset: set new data_element by name."""
    ds = Dataset()
    ds.TreatmentMachineName = "unit #1"
    data_element = ds[0x300a, 0x00b2]
    assert "unit #1" == data_element.value
    assert "SH" == data_element.VR
