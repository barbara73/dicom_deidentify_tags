De-Identify DICOM Tags
======================

Get date elements
-----------------
Get all date elements from data set, which will then be de-identified with a day shift.

De-identify dates
-----------------
De-identify all dates with a time-shift. If no time shift is given, then date and time is set to None.

Add de-identified UID's
-----------------------
A new SOP instance UID is created for each image. You can add predefined UID's for study and series, otherwise one will be set. For same series, the new created UID's should be the same!
With a look up table you can ensure that.

Get de-identified data set
--------------------------
Returns the de-identified data set, based on the given rule set.
