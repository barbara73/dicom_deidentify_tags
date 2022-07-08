"""
Factory Dataset
"""
from pydicom.dataset import Dataset
from pydicom.tag import Tag


def quick_dataset(*_, **kwargs) -> Dataset:
    """A dataset with keyword args as tagname - value pairs
    For example:
    >>> ds = quick_dataset(PatientName='Jane', StudyDescription='Test')
    >>> ds.PatientName
    'Jane'
    >>> ds.StudyDescription
    'Test'
    Raises
    ------
    ValueError
        If any input key is not a valid DICOM keyword
    """
    dataset = Dataset()
    for tagname, value in kwargs.items():
        Tag(tagname)  # assert valid dicom keyword. pydicom will not do this.
        dataset.__setattr__(tagname, value)
    return dataset
