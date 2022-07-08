# De-Identify DICOM

This package is for de-identifying DICOM tags.

### Look-up
You can add

- filename
- deid_patient_id
- deid_study_id
- deid_series_id
- deid_sop_uid
- time_shift (in days)

to the look-up. If lookup is empty, all the uids are created. 
Date and times are then deleted entirely.

### De-Identify
- get date elements: get all date elements in data set
- de-identify dates: de-identify all dates with a time-shift 
(if no time shift is given, then date and time is set to None)
- add de-identified uid's: a new SOP instance UID is created 
(you can add predefined uids for study and series, otherwise one will be set 
but take care: for same series, the uid should be the same and so for the study and patient)
- get de-identified data set: returns the de-identified data set, based on the rule set given.

### Rule sets
This is based on idiscore package. Rule set adapted 
(NEMA rule set without dates, which are handled separately)
