import json
from pathlib import Path

import pytest
from dicomgenerator.factory import DataElementFactory, CTDatasetFactory
from pydicom import Dataset
from pydicom.uid import ExplicitVRLittleEndian

from src.dicomdeidentifier.deidentify_dicom import LookupID


@pytest.fixture
def a_dataset() -> Dataset:
    """Tiny Dataset that can be used with some_rules and a_core_with_some_rules"""

    dataset = Dataset()
    dataset.add(DataElementFactory(tag="PatientID", value="12345"))
    dataset.add(DataElementFactory(tag="Modality", value="CT"))
    dataset.add(DataElementFactory(tag="PatientName", value="Martha"))
    dataset.add(DataElementFactory(tag=(0x5010, 0x3000), value=b"Sensitive data"))
    dataset.add(DataElementFactory(tag=(0x1013, 0x0001), value=b"private tag"))
    block = dataset.private_block(0x00B1, "TestCreator", create=True)
    block.add_new(0x01, "SH", "my testvalue")
    return dataset


@pytest.fixture
def datetime_dataset():
    """A dataset for testing date and time management"""
    dataset = Dataset()
    elements = [
        DataElementFactory(tag="PatientBirthDate", value="19800501"),           # (0010, 0030)
        DataElementFactory(tag="AcquisitionDate", value="19800501"),            # (0008, 0022)
        DataElementFactory(tag="AcquisitionDateTime", value="19800501163601"),  # (0008, 002a)
        DataElementFactory(tag="AcquisitionTime", value="163601"),              # (0008, 0032)
        DataElementFactory(tag="SeriesDate", value="19730825121212.120000"),
        DataElementFactory(tag="StudyDate", value="20190202"),

    ]
    for element in elements:
        dataset.add(element)
    return dataset


@pytest.fixture
def a_lookup():
    return LookupID(deid_patient_id='a_patient_id',
                    deid_series_uid='2.25.22070338010590029158579357354431',
                    deid_study_uid='1.25.220703380105900291585793573',
                    deid_sop_uid='2.25.22070338010522222222222',
                    time_shift=1,
                    filename='a_filename'
                    )


@pytest.fixture
def wrong_type_lookup():
    return LookupID(deid_patient_id='a_patient_id',
                    deid_series_uid='a_series_uid',
                    deid_study_uid='a_study_uid',
                    deid_sop_uid='a_deidentified_SOP',
                    time_shift='e',
                    filename='a_filename'
                    )

@pytest.fixture
def a_dataset_with_transfer_syntax():
    """Transfer Syntax is needed for interpreting PixelData. This is not
    recorded with CTDatasetFactory()
    """
    dataset = CTDatasetFactory()
    dataset.file_meta = Dataset()
    dataset.file_meta.TransferSyntaxUID = ExplicitVRLittleEndian
    return dataset
