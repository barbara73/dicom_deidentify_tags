Introduction
============


This package is for de-identifying DICOM tags.

Look-up
-------
You can add your predefined

- filename
- deid_patient_id
- deid_study_id
- deid_series_id
- deid_sop_uid
- time_shift (in days)

to the look-up. If lookup is empty, all the UID's are created.
Date and times are then deleted entirely.

Take care: the new UID's should be the same for the same studies and series from one patient.

