"""
Custom rule sets.

Adapted rule set from NEMA (Argos) with time shifts (implemented).
If time shift is 0 or None, no dates and times are saved.
"""
from idiscore.nema import RuleSet, Rule
from idiscore.identifiers import SingleTag, RepeatingGroup
from idiscore.operators import Remove, Keep, Empty, Replace

timeshift_custom_ruleset = RuleSet(
    name="Time-shift Custom RuleSet (NEMA adapted)",
    rules=[
        Rule(SingleTag("00080050"), Empty()),               # Accession Number
        Rule(SingleTag("00184000"), Remove()),              # Acquisition Comments
        Rule(SingleTag("00400555"), Remove()),              # Acquisition Context Sequence
        Rule(SingleTag("00181400"), Remove()),              # Acquisition Device Processing Description
        Rule(SingleTag("001811BB"), Replace()),             # Acquisition Field Of View Label
        Rule(SingleTag("00189424"), Remove()),              # Acquisition Protocol Description
        Rule(SingleTag("00404035"), Remove()),              # Actual Human Performers Sequence
        Rule(SingleTag("001021B0"), Remove()),              # Additional Patient History
        Rule(SingleTag("0040A353"), Remove()),              # Address (Trial)
        Rule(SingleTag("00380010"), Remove()),              # Admission ID
        Rule(SingleTag("00081084"), Remove()),              # Admitting Diagnoses Code Sequence
        Rule(SingleTag("00081080"), Remove()),              # Admitting Diagnoses Description
        Rule(SingleTag("00001000"), Remove()),              # Affected SOP Instance UID
        Rule(SingleTag("00102110"), Remove()),              # Allergies
        Rule(SingleTag("40000010"), Remove()),              # Arbitrary
        Rule(SingleTag("0040A078"), Remove()),              # Author Observer Sequence
        Rule(SingleTag("22000005"), Remove()),              # Barcode Value
        Rule(SingleTag("300A00C3"), Remove()),              # Beam Description
        Rule(SingleTag("300A00DD"), Remove()),              # Bolus Description
        Rule(SingleTag("00101081"), Remove()),              # Branch of Service
        Rule(SingleTag("0016004D"), Remove()),              # Camera Owner Name
        Rule(SingleTag("00181007"), Remove()),              # Cassette ID
        Rule(SingleTag("00120060"), Empty()),               # Clinical Trial Coordinating Center Name
        Rule(SingleTag("00120082"), Remove()),              # Clinical Trial Protocol Ethics Committee Approval Number
        Rule(SingleTag("00120081"), Replace()),             # Clinical Trial Protocol Ethics Committee Name
        Rule(SingleTag("00120020"), Replace()),             # Clinical Trial Protocol ID
        Rule(SingleTag("00120021"), Empty()),               # Clinical Trial Protocol Name
        Rule(SingleTag("00120072"), Remove()),              # Clinical Trial Series Description
        Rule(SingleTag("00120071"), Remove()),              # Clinical Trial Series ID
        Rule(SingleTag("00120030"), Empty()),               # Clinical Trial Site ID
        Rule(SingleTag("00120031"), Empty()),               # Clinical Trial Site Name
        Rule(SingleTag("00120010"), Replace()),             # Clinical Trial Sponsor Name
        Rule(SingleTag("00120040"), Replace()),             # Clinical Trial Subject ID
        Rule(SingleTag("00120042"), Replace()),             # Clinical Trial Subject Reading ID
        Rule(SingleTag("00120051"), Remove()),              # Clinical Trial Time Point Description
        Rule(SingleTag("00120050"), Empty()),               # Clinical Trial Time Point ID
        Rule(SingleTag("00400310"), Remove()),              # Comments on Radiation Dose
        Rule(SingleTag("00400280"), Remove()),              # Comments on the Performed Procedure Step
        Rule(SingleTag("300A02EB"), Remove()),              # Compensator Description
        Rule(SingleTag("00209161"), Remove()),              # Concatenation UID
        Rule(SingleTag("3010000F"), Empty()),               # Conceptual Volume Combination Description
        Rule(SingleTag("30100017"), Empty()),               # Conceptual Volume Description
        Rule(SingleTag("30100006"), Remove()),              # Conceptual Volume UID
        Rule(SingleTag("00403001"), Remove()),              # Confidentiality Constraint on Patient Data Description
        Rule(SingleTag("30100013"), Remove()),              # Constituent Conceptual Volume UID
        Rule(SingleTag("0008009C"), Empty()),               # Consulting Physician's Name
        Rule(SingleTag("0008009D"), Remove()),              # Consulting Physician Identification Sequence
        Rule(SingleTag("0050001B"), Remove()),              # Container Component ID
        Rule(SingleTag("0040051A"), Remove()),              # Container Description
        Rule(SingleTag("00400512"), Replace()),             # Container Identifier
        Rule(SingleTag("00700086"), Remove()),              # Content Creator's Identification Code Sequence
        Rule(SingleTag("00700084"), Replace()),             # Content Creator's Name
        Rule(SingleTag("0040A730"), Replace()),             # Content Sequence
        Rule(SingleTag("0008010D"), Remove()),              # Context Group Extension Creator UID
        Rule(SingleTag("00180010"), Replace()),             # Contrast/Bolus Agent
        Rule(SingleTag("0018A003"), Remove()),              # Contribution Description
        Rule(SingleTag("00102150"), Remove()),              # Country of Residence
        Rule(SingleTag("00089123"), Remove()),              # Creator Version UID
        Rule(SingleTag("0040A307"), Remove()),              # Current Observer (Trial)
        Rule(SingleTag("00380300"), Remove()),              # Current Patient Location
        Rule(SingleTag("0040A07C"), Remove()),              # Custodial Organization Sequence
        Rule(SingleTag("FFFCFFFC"), Remove()),              # Data Set Trailing Padding
        Rule(SingleTag("0018937F"), Remove()),              # Decomposition Description
        Rule(SingleTag("00082111"), Remove()),              # Derivation Description
        Rule(SingleTag("0018700A"), Remove()),              # Detector ID
        Rule(SingleTag("3010001B"), Empty()),               # Device Alternate Identifier
        Rule(SingleTag("00500020"), Remove()),              # Device Description
        Rule(SingleTag("3010002D"), Replace()),             # Device Label
        Rule(SingleTag("00181000"), Remove()),              # Device Serial Number
        Rule(SingleTag("0016004B"), Remove()),              # Device Setting Description
        Rule(SingleTag("00181002"), Remove()),              # Device UID
        Rule(SingleTag("FFFAFFFA"), Remove()),              # Digital Signatures Sequence
        Rule(SingleTag("04000100"), Remove()),              # Digital Signature UID
        Rule(SingleTag("00209164"), Remove()),              # Dimension Organization UID
        Rule(SingleTag("00380040"), Remove()),              # Discharge Diagnosis Description
        Rule(SingleTag("4008011A"), Remove()),              # Distribution Address
        Rule(SingleTag("40080119"), Remove()),              # Distribution Name
        Rule(SingleTag("300A0016"), Remove()),              # Dose Reference Description
        Rule(SingleTag("300A0013"), Remove()),              # Dose Reference UID
        Rule(SingleTag("3010006E"), Remove()),              # Dosimetric Objective UID
        Rule(SingleTag("30100037"), Remove()),              # Entity Description
        Rule(SingleTag("30100035"), Replace()),             # Entity Label
        Rule(SingleTag("30100038"), Replace()),             # Entity Long Label
        Rule(SingleTag("30100036"), Remove()),              # Entity Name
        Rule(SingleTag("300A0676"), Remove()),              # Equipment Frame of Reference Description
        Rule(SingleTag("00102160"), Remove()),              # Ethnic Group
        Rule(SingleTag("00080058"), Remove()),              # Failed SOP Instance UID List
        Rule(SingleTag("0070031A"), Remove()),              # Fiducial UID
        Rule(SingleTag("00402017"), Empty()),               # Filler Order Number / Imaging Service Request
        Rule(SingleTag("300A0196"), Remove()),              # Fixation Device Description
        Rule(SingleTag("00340002"), Replace()),             # Flow Identifier
        Rule(SingleTag("00340001"), Replace()),             # Flow Identifier Sequence
        Rule(SingleTag("3010007F"), Empty()),               # Fractionation Notes
        Rule(SingleTag("300A0072"), Remove()),              # Fraction Group Description
        Rule(SingleTag("00209158"), Remove()),              # Frame Comments
        Rule(SingleTag("00200052"), Remove()),              # Frame of Reference UID
        Rule(SingleTag("00181008"), Remove()),              # Gantry ID
        Rule(SingleTag("00181005"), Remove()),              # Generator ID
        Rule(SingleTag("00160076"), Remove()),              # GPS Altitude
        Rule(SingleTag("00160075"), Remove()),              # GPS Altitude Ref
        Rule(SingleTag("0016008C"), Remove()),              # GPS Area Information
        Rule(SingleTag("00160088"), Remove()),              # GPS Dest Bearing
        Rule(SingleTag("00160087"), Remove()),              # GPS Dest Bearing Ref
        Rule(SingleTag("0016008A"), Remove()),              # GPS Dest Distance
        Rule(SingleTag("00160089"), Remove()),              # GPS Dest Distance Ref
        Rule(SingleTag("00160084"), Remove()),              # GPS Dest Latitude
        Rule(SingleTag("00160083"), Remove()),              # GPS Dest Latitude Ref
        Rule(SingleTag("00160086"), Remove()),              # GPS Dest Longitude
        Rule(SingleTag("00160085"), Remove()),              # GPS Dest Longitude Ref
        Rule(SingleTag("0016008E"), Remove()),              # GPS Differential
        Rule(SingleTag("0016007B"), Remove()),              # GPS DOP
        Rule(SingleTag("00160081"), Remove()),              # GPS Img Direction
        Rule(SingleTag("00160080"), Remove()),              # GPS Img Direction Ref
        Rule(SingleTag("00160072"), Remove()),              # GPS Latitude
        Rule(SingleTag("00160071"), Remove()),              # GPS Latitude Ref
        Rule(SingleTag("00160074"), Remove()),              # GPS Longitude
        Rule(SingleTag("00160073"), Remove()),              # GPS Longitude Ref
        Rule(SingleTag("00160082"), Remove()),              # GPS Map Datum
        Rule(SingleTag("0016007A"), Remove()),              # GPS Measure Mode
        Rule(SingleTag("0016008B"), Remove()),              # GPS Processing Method
        Rule(SingleTag("00160078"), Remove()),              # GPS Satellites
        Rule(SingleTag("0016007D"), Remove()),              # GPS Speed
        Rule(SingleTag("0016007C"), Remove()),              # GPS Speed Ref
        Rule(SingleTag("00160079"), Remove()),              # GPS Status
        Rule(SingleTag("0016007F"), Remove()),              # GPS Track
        Rule(SingleTag("0016007E"), Remove()),              # GPS Track Ref
        Rule(SingleTag("00160070"), Remove()),              # GPS Version ID
        Rule(SingleTag("00700001"), Replace()),             # Graphic Annotation Sequence
        Rule(SingleTag("00404037"), Remove()),              # Human Performer's Name
        Rule(SingleTag("00404036"), Remove()),              # Human Performer's Organization
        Rule(SingleTag("00880200"), Remove()),              # Icon Image Sequence
        Rule(SingleTag("00084000"), Remove()),              # Identifying Comments
        Rule(SingleTag("00204000"), Remove()),              # Image Comments
        Rule(SingleTag("00284000"), Remove()),              # Image Presentation Comments
        Rule(SingleTag("00402400"), Remove()),              # Imaging Service Request Comments
        Rule(SingleTag("40080300"), Remove()),              # Impressions
        Rule(SingleTag("00080014"), Remove()),              # Instance Creator UID
        Rule(SingleTag("04000600"), Remove()),              # Instance Origin Status
        Rule(SingleTag("00080081"), Remove()),              # Institution Address
        Rule(SingleTag("00081040"), Remove()),              # Institutional Department Name
        Rule(SingleTag("00081041"), Remove()),              # Institutional Department Type Code Sequence
        Rule(SingleTag("00080082"), Remove()),              # Institution Code Sequence
        Rule(SingleTag("00080080"), Remove()),              # Institution Name
        Rule(SingleTag("00101050"), Remove()),              # Insurance Plan Identification
        Rule(SingleTag("00401011"), Remove()),              # Intended Recipients of Results Identification Sequence
        Rule(SingleTag("300A0742"), Replace()),             # Interlock Description
        Rule(SingleTag("300A0783"), Replace()),             # Interlock Origin Description
        Rule(SingleTag("40080111"), Remove()),              # Interpretation Approver Sequence
        Rule(SingleTag("4008010C"), Remove()),              # Interpretation Author
        Rule(SingleTag("40080115"), Remove()),              # Interpretation Diagnosis Description
        Rule(SingleTag("40080202"), Remove()),              # Interpretation ID Issuer
        Rule(SingleTag("40080102"), Remove()),              # Interpretation Recorder
        Rule(SingleTag("4008010B"), Remove()),              # Interpretation Text
        Rule(SingleTag("4008010A"), Remove()),              # Interpretation Transcriber
        Rule(SingleTag("00083010"), Remove()),              # Irradiation Event UID
        Rule(SingleTag("00380011"), Remove()),              # Issuer of Admission ID
        Rule(SingleTag("00380014"), Remove()),              # Issuer of Admission ID Sequence
        Rule(SingleTag("00100021"), Remove()),              # Issuer of Patient ID
        Rule(SingleTag("00380061"), Remove()),              # Issuer of Service Episode ID
        Rule(SingleTag("00380064"), Remove()),              # Issuer of Service Episode ID Sequence
        Rule(SingleTag("00400513"), Empty()),               # Issuer of the Container Identifier Sequence
        Rule(SingleTag("00400562"), Empty()),               # Issuer of the Specimen Identifier Sequence
        Rule(SingleTag("00183100"), Empty()),               # IVUS Acquisition
        Rule(SingleTag("22000002"), Remove()),              # Label Text
        Rule(SingleTag("00281214"), Remove()),              # Large Palette Color Lookup Table UID
        Rule(SingleTag("0016004F"), Remove()),              # Lens Make
        Rule(SingleTag("00160050"), Remove()),              # Lens Model
        Rule(SingleTag("00160051"), Remove()),              # Lens Serial Number
        Rule(SingleTag("0016004E"), Remove()),              # Lens Specification
        Rule(SingleTag("00500021"), Remove()),              # Long Device Description
        Rule(SingleTag("04000404"), Remove()),              # MAC
        Rule(SingleTag("0016002B"), Remove()),              # Maker Note
        Rule(SingleTag("0018100B"), Remove()),              # Manufacturer's Device Class UID
        Rule(SingleTag("30100043"), Empty()),               # Manufacturer's Device Identifier
        Rule(SingleTag("00102000"), Remove()),              # Medical Alerts
        Rule(SingleTag("00101090"), Remove()),              # Medical Record Locator
        Rule(SingleTag("00101080"), Remove()),              # Military Rank
        Rule(SingleTag("04000550"), Remove()),              # Modified Attributes Sequence
        Rule(SingleTag("00203406"), Remove()),              # Modified Image Description
        Rule(SingleTag("00203401"), Remove()),              # Modifying Device ID
        Rule(SingleTag("0018937B"), Remove()),              # Multi-energy Acquisition Description
        Rule(SingleTag("003A0310"), Remove()),              # Multiplex Group UID
        Rule(SingleTag("00081060"), Remove()),              # Name of Physician(s) Reading Study
        Rule(SingleTag("00401010"), Remove()),              # Names of Intended Recipients of Results
        Rule(SingleTag("04000551"), Remove()),              # Nonconforming Modified Attributes Sequence
        Rule(SingleTag("04000552"), Remove()),              # Nonconforming Data Element Value
        Rule(SingleTag("0040A402"), Remove()),              # Observation Subject UID (Trial)
        Rule(SingleTag("0040A171"), Remove()),              # Observation UID
        Rule(SingleTag("00102180"), Remove()),              # Occupation
        Rule(SingleTag("00081072"), Remove()),              # Operator Identification Sequence
        Rule(SingleTag("00081070"), Remove()),              # Operators' Name
        Rule(SingleTag("00402010"), Remove()),              # Order Callback Phone Number
        Rule(SingleTag("00402011"), Remove()),              # Order Callback Telecom Information
        Rule(SingleTag("00402008"), Remove()),              # Order Entered By
        Rule(SingleTag("00402009"), Remove()),              # Order Enterer's Location
        Rule(SingleTag("04000561"), Remove()),              # Original Attributes Sequence
        Rule(SingleTag("00101000"), Remove()),              # Other Patient IDs
        Rule(SingleTag("00101002"), Remove()),              # Other Patient IDs Sequence
        Rule(SingleTag("00101001"), Remove()),              # Other Patient Names
        Rule(SingleTag("00281199"), Remove()),              # Palette Color Lookup Table UID
        Rule(SingleTag("0040A07A"), Remove()),              # Participant Sequence
        Rule(SingleTag("00101040"), Remove()),              # Patient's Address
        Rule(SingleTag("00101010"), Empty()),               # Patient's Age
        Rule(SingleTag("00101005"), Remove()),              # Patient's Birth Name
        Rule(SingleTag("00100032"), Remove()),              # Patient's Birth Time
        Rule(SingleTag("00380400"), Remove()),              # Patient's Institution Residence
        Rule(SingleTag("00100050"), Remove()),              # Patient's Insurance Plan Code Sequence
        Rule(SingleTag("00101060"), Remove()),              # Patient's Mother's Birth Name
        Rule(SingleTag("00100010"), Empty()),               # Patient's Name
        Rule(SingleTag("00100101"), Remove()),              # Patient's Primary Language Code Sequence
        Rule(SingleTag("00100102"), Remove()),              # Patient's Primary Language Modifier Code Sequence
        Rule(SingleTag("001021F0"), Remove()),              # Patient's Religious Preference
        Rule(SingleTag("00100040"), Empty()),               # Patient's Sex
        Rule(SingleTag("00102203"), Remove()),              # Patient's Sex Neutered
        Rule(SingleTag("00101020"), Remove()),              # Patient's Size
        Rule(SingleTag("00102155"), Remove()),              # Patient's Telecom Information
        Rule(SingleTag("00102154"), Remove()),              # Patient's Telephone Numbers
        Rule(SingleTag("00101030"), Keep()),                # Patient's Weight
        Rule(SingleTag("00104000"), Remove()),              # Patient Comments
        Rule(SingleTag("300A0650"), Remove()),              # Patient Setup UID
        Rule(SingleTag("00380500"), Remove()),              # Patient State
        Rule(SingleTag("00401004"), Remove()),              # Patient Transport Arrangements
        Rule(SingleTag("00400243"), Remove()),              # Performed Location
        Rule(SingleTag("00400254"), Remove()),              # Performed Procedure Step Description
        Rule(SingleTag("00400253"), Remove()),              # Performed Procedure Step ID
        Rule(SingleTag("00400241"), Remove()),              # Performed Station AE Title
        Rule(SingleTag("00404030"), Remove()),              # Performed Station Geographic Location Code Sequence
        Rule(SingleTag("00400242"), Remove()),              # Performed Station Name
        Rule(SingleTag("00404028"), Remove()),              # Performed Station Name Code Sequence
        Rule(SingleTag("00081050"), Remove()),              # Performing Physician's Name
        Rule(SingleTag("00081052"), Remove()),              # Performing Physician Identification Sequence
        Rule(SingleTag("00401102"), Remove()),              # Person's Address
        Rule(SingleTag("00401104"), Remove()),              # Person's Telecom Information
        Rule(SingleTag("00401103"), Remove()),              # Person's Telephone Numbers
        Rule(SingleTag("00401101"), Replace()),             # Person Identification Code Sequence
        Rule(SingleTag("0040A123"), Replace()),             # Person Name
        Rule(SingleTag("00081048"), Remove()),              # Physician(s) of Record
        Rule(SingleTag("00081049"), Remove()),              # Physician(s) of Record Identification Sequence
        Rule(SingleTag("00081062"), Remove()),              # Physician(s) Reading Study Identification Sequence
        Rule(SingleTag("40080114"), Remove()),              # Physician Approving Interpretation
        Rule(SingleTag("00402016"), Empty()),               # Placer Order Number / Imaging Service Request
        Rule(SingleTag("00181004"), Remove()),              # Plate ID
        Rule(SingleTag("001021C0"), Remove()),              # Pregnancy Status
        Rule(SingleTag("00400012"), Remove()),              # Pre-Medication
        Rule(SingleTag("300A000E"), Remove()),              # Prescription Description
        Rule(SingleTag("3010007B"), Empty()),               # Prescription Notes
        Rule(SingleTag("30100081"), Empty()),               # Prescription Notes Sequence
        Rule(SingleTag("00701101"), Remove()),              # Presentation Display Collection UID
        Rule(SingleTag("00701102"), Remove()),              # Presentation Sequence Collection UID
        Rule(SingleTag("30100061"), Remove()),              # Prior Treatment Dose Description
        Rule(SingleTag("00181030"), Remove()),              # Protocol Name
        Rule(SingleTag("300A0619"), Replace()),             # Radiation Dose Identification Label
        Rule(SingleTag("300A0623"), Replace()),             # Radiation Dose In-Vivo Measurement Label
        Rule(SingleTag("300A067D"), Empty()),               # Radiation Generation Mode Description
        Rule(SingleTag("300A067C"), Replace()),             # Radiation Generation Mode Label
        Rule(SingleTag("300C0113"), Remove()),              # Reason for Omission Description
        Rule(SingleTag("0040100A"), Remove()),              # Reason for Requested Procedure Code Sequence
        Rule(SingleTag("00321030"), Remove()),              # Reason for Study
        Rule(SingleTag("3010005C"), Empty()),               # Reason for Superseding
        Rule(SingleTag("00402001"), Remove()),              # Reason for the Imaging Service Request
        Rule(SingleTag("00401002"), Remove()),              # Reason for the Requested Procedure
        Rule(SingleTag("00321066"), Remove()),              # Reason for Visit
        Rule(SingleTag("00321067"), Remove()),              # Reason for Visit Code Sequence
        Rule(SingleTag("3010000B"), Remove()),              # Referenced Conceptual Volume UID
        Rule(SingleTag("04000402"), Remove()),              # Referenced Digital Signature Sequence
        Rule(SingleTag("300A0083"), Remove()),              # Referenced Dose Reference UID
        Rule(SingleTag("3010006F"), Remove()),              # Referenced Dosimetric Objective UID
        Rule(SingleTag("30100031"), Remove()),              # Referenced Fiducials UID
        Rule(SingleTag("30060024"), Remove()),              # Referenced Frame of Reference UID
        Rule(SingleTag("00404023"), Remove()),              # Referenced General Purpose ...
        Rule(SingleTag("00081140"), Remove()),              # Referenced Image Sequence
        Rule(SingleTag("0040A172"), Remove()),              # Referenced Observation UID (Trial)
        Rule(SingleTag("00380004"), Remove()),              # Referenced Patient Alias Sequence
        Rule(SingleTag("00101100"), Remove()),              # Referenced Patient Photo Sequence
        Rule(SingleTag("00081120"), Remove()),              # Referenced Patient Sequence
        Rule(SingleTag("00081111"), Remove()),              # Referenced Performed Procedure Step Sequence
        Rule(SingleTag("04000403"), Remove()),              # Referenced SOP Instance MAC Sequence
        Rule(SingleTag("00081155"), Remove()),              # Referenced SOP Instance UID
        Rule(SingleTag("00041511"), Remove()),              # Referenced SOP Instance UID in File
        Rule(SingleTag("00081110"), Remove()),              # Referenced Study Sequence
        Rule(SingleTag("00081115"), Remove()),              # Referenced Series Sequence
        Rule(SingleTag("00080096"), Remove()),              # Referring Physician's Identification Sequence
        Rule(SingleTag("00080092"), Remove()),              # Referring Physician's Address
        Rule(SingleTag("00080090"), Empty()),               # Referring Physician's Name
        Rule(SingleTag("00080094"), Remove()),              # Referring Physician's Telephone Numbers
        Rule(SingleTag("00080096"), Remove()),              # Referring Physician Identification Sequence
        Rule(SingleTag("00102152"), Remove()),              # Region of Residence
        Rule(SingleTag("300600C2"), Remove()),              # Related Frame of Reference UID
        Rule(SingleTag("00081250"), Remove()),              # Related Series Sequence Attribute
        Rule(SingleTag("00400275"), Empty()),               # Request Attributes Sequence
        Rule(SingleTag("00321070"), Remove()),              # Requested Contrast Agent
        Rule(SingleTag("00401400"), Remove()),              # Requested Procedure Comments
        Rule(SingleTag("00321060"), Remove()),              # Requested Procedure Description
        Rule(SingleTag("00401001"), Remove()),              # Requested Procedure ID
        Rule(SingleTag("00401005"), Remove()),              # Requested Procedure Location
        Rule(SingleTag("00189937"), Remove()),              # Requested Series Description
        Rule(SingleTag("00001001"), Remove()),              # Requested SOP Instance UID
        Rule(SingleTag("00321032"), Remove()),              # Requesting Physician
        Rule(SingleTag("00321033"), Remove()),              # Requesting Service
        Rule(SingleTag("00189185"), Remove()),              # Respiratory Motion Compensation Technique Description
        Rule(SingleTag("00102299"), Remove()),              # Responsible Organization
        Rule(SingleTag("00102297"), Remove()),              # Responsible Person
        Rule(SingleTag("40084000"), Remove()),              # Results Comments
        Rule(SingleTag("40080118"), Remove()),              # Results Distribution List Sequence
        Rule(SingleTag("40080042"), Remove()),              # Results ID Issuer
        Rule(SingleTag("300E0008"), Remove()),              # Reviewer Name
        Rule(SingleTag("30060028"), Keep()),                # ROI Description
        Rule(SingleTag("30060038"), Remove()),              # ROI Generation Description
        Rule(SingleTag("300600A6"), Empty()),               # ROI Interpreter
        Rule(SingleTag("30060026"), Keep()),                # ROI Name
        Rule(SingleTag("30060088"), Remove()),              # ROI Observation Description
        Rule(SingleTag("30060085"), Remove()),              # ROI Observation Label
        Rule(SingleTag("300A0615"), Empty()),               # RT Accessory Device Slot ID
        Rule(SingleTag("300A0611"), Empty()),               # RT Accessory Holder Slot ID
        Rule(SingleTag("3010005A"), Empty()),               # RT Physician Intent Narrative
        Rule(SingleTag("300A0004"), Remove()),              # RT Plan Description
        Rule(SingleTag("300A0002"), Replace()),             # RT Plan Label
        Rule(SingleTag("300A0003"), Remove()),              # RT Plan Name
        Rule(SingleTag("30100054"), Replace()),             # RT Prescription Label
        Rule(SingleTag("300A062A"), Replace()),             # RT Tolerance Set Label
        Rule(SingleTag("30100056"), Remove()),              # RT Treatment Approach Label
        Rule(SingleTag("3010003B"), Remove()),              # RT Treatment Phase UID
        Rule(SingleTag("30060014"), Remove()),              # RT Referenced Series Sequence
        Rule(SingleTag("30060012"), Remove()),              # RT Referenced Study Sequence
        Rule(SingleTag("00404034"), Remove()),              # Scheduled Human Performers Sequence
        Rule(SingleTag("0038001E"), Remove()),              # Scheduled Patient Institution Residence
        Rule(SingleTag("00400006"), Remove()),              # Scheduled Performing Physician's Name
        Rule(SingleTag("0040000B"), Remove()),              # Scheduled Performing Physician Identification Sequence
        Rule(SingleTag("00400007"), Remove()),              # Scheduled Procedure Step Description
        Rule(SingleTag("00400009"), Remove()),              # Scheduled Procedure Step ID
        Rule(SingleTag("00400011"), Remove()),              # Scheduled Procedure Step Location
        Rule(SingleTag("00400001"), Remove()),              # Scheduled Station AE Title
        Rule(SingleTag("00404027"), Remove()),              # Scheduled Station Geographic Location Code Sequence
        Rule(SingleTag("00400010"), Remove()),              # Scheduled Station Name
        Rule(SingleTag("00404025"), Remove()),              # Scheduled Station Name Code Sequence
        Rule(SingleTag("00321020"), Remove()),              # Scheduled Study Location
        Rule(SingleTag("00321021"), Remove()),              # Scheduled Study Location AE Title
        Rule(SingleTag("0008103E"), Remove()),              # Series Description
        Rule(SingleTag("00380062"), Remove()),              # Service Episode Description
        Rule(SingleTag("00380060"), Remove()),              # Service Episode ID
        Rule(SingleTag("300A01B2"), Remove()),              # Setup Technique Description
        Rule(SingleTag("300A01A6"), Remove()),              # Shielding Device Description
        Rule(SingleTag("004006FA"), Remove()),              # Slide Identifier
        Rule(SingleTag("001021A0"), Remove()),              # Smoking Status
        Rule(SingleTag("30100015"), Remove()),              # Source Conceptual Volume UID
        Rule(SingleTag("00340005"), Replace()),             # Source Identifier
        Rule(SingleTag("00082112"), Remove()),              # Source Image Sequence
        Rule(SingleTag("300A0216"), Remove()),              # Source Manufacturer
        Rule(SingleTag("30080105"), Remove()),              # Source Serial Number
        Rule(SingleTag("00380050"), Remove()),              # Special Needs
        Rule(SingleTag("0040050A"), Remove()),              # Specimen Accession Number
        Rule(SingleTag("00400602"), Remove()),              # Specimen Detailed Description
        Rule(SingleTag("00400551"), Replace()),             # Specimen Identifier
        Rule(SingleTag("00400610"), Empty()),               # Specimen Preparation Sequence
        Rule(SingleTag("00400600"), Remove()),              # Specimen Short Description
        Rule(SingleTag("00400554"), Remove()),              # Specimen UID
        Rule(SingleTag("00081010"), Remove()),              # Station Name
        Rule(SingleTag("00880140"), Remove()),              # Storage Media File-set UID
        Rule(SingleTag("30060006"), Remove()),              # Structure Set Description
        Rule(SingleTag("30060002"), Replace()),             # Structure Set Label
        Rule(SingleTag("30060004"), Remove()),              # Structure Set Name
        Rule(SingleTag("00324000"), Remove()),              # Study Comments
        Rule(SingleTag("00081030"), Remove()),              # Study Description
        Rule(SingleTag("00200010"), Empty()),               # Study ID
        Rule(SingleTag("00320012"), Remove()),              # Study ID Issuer
        Rule(SingleTag("00200200"), Remove()),              # Synchronization Frame of Reference UID
        Rule(SingleTag("00182042"), Remove()),              # Target UID
        Rule(SingleTag("0040A354"), Remove()),              # Telephone Number (Trial)
        Rule(SingleTag("0040DB0D"), Remove()),              # Template Extension Creator UID
        Rule(SingleTag("0040DB0C"), Remove()),              # Template Extension Organization UID
        Rule(SingleTag("40004000"), Remove()),              # Text Comments
        Rule(SingleTag("20300020"), Remove()),              # Text String
        Rule(SingleTag("00080201"), Remove()),              # Timezone Offset From UTC
        Rule(SingleTag("00880910"), Remove()),              # Topic Author
        Rule(SingleTag("00880912"), Remove()),              # Topic Keywords
        Rule(SingleTag("00880906"), Remove()),              # Topic Subject
        Rule(SingleTag("00880904"), Remove()),              # Topic Title
        Rule(SingleTag("00620021"), Remove()),              # Tracking UID
        Rule(SingleTag("00081195"), Remove()),              # Transaction UID
        Rule(SingleTag("00185011"), Remove()),              # Transducer Identification Sequence
        Rule(SingleTag("300A00B2"), Remove()),              # Treatment Machine Name
        Rule(SingleTag("300A0608"), Replace()),             # Treatment Position Group Label
        Rule(SingleTag("300A0609"), Remove()),              # Treatment Position Group UID
        Rule(SingleTag("300A0700"), Remove()),              # Treatment Session UID
        Rule(SingleTag("30100077"), Replace()),             # Treatment Site
        Rule(SingleTag("3010007A"), Empty()),               # Treatment Technique Notes
        Rule(SingleTag("300A0734"), Replace()),             # Treatment Tolerance Violation Description
        Rule(SingleTag("0018100A"), Remove()),              # UDI Sequence
        Rule(SingleTag("0040A124"), Remove()),              # UID
        Rule(SingleTag("00181009"), Remove()),              # Unique Device Identifier
        Rule(SingleTag("30100033"), Replace()),             # User Content Label
        Rule(SingleTag("30100034"), Replace()),             # User Content Long Label
        Rule(SingleTag("0040A352"), Remove()),              # Verbal Source (Trial)
        Rule(SingleTag("0040A358"), Remove()),              # Verbal Source Identifier Code Sequence (Trial)
        Rule(SingleTag("0040A088"), Empty()),               # Verifying Observer Identification Code Sequence
        Rule(SingleTag("0040A075"), Replace()),             # Verifying Observer Name
        Rule(SingleTag("0040A073"), Replace()),             # Verifying Observer Sequence
        Rule(SingleTag("0040A027"), Replace()),             # Verifying Organization
        Rule(SingleTag("00384000"), Remove()),              # Visit Comments
        Rule(SingleTag("00189371"), Replace()),             # X-Ray Detector ID
        Rule(SingleTag("00189373"), Remove()),              # X-Ray Detector Label
        Rule(SingleTag("00189367"), Replace()),             # X-Ray Source ID
        Rule(SingleTag("00120063"), Keep()),                # De-identification Method
        Rule(SingleTag("00120064"), Keep()),                # De-identification Method Code Sequence
        Rule(SingleTag("00020016"), Remove()),              # Source Application Entity Title
        Rule(SingleTag("00400340"), Remove()),              # Performed Series Sequence
        Rule(SingleTag("00400252"), Remove()),              # Performed Procedure Step Status
        Rule(SingleTag("00400255"), Remove()),              # Performed Procedure Step Description
        Rule(RepeatingGroup("50xx,xxxx"), Remove()),        # Curve data
        Rule(RepeatingGroup("60xx,x000"), Remove()),        # Overlay Comments
        Rule(RepeatingGroup("4008,xxxx"), Remove()),        # Result Comments
    ],
)

no_times_ruleset = RuleSet(
    name="Rule set for deleting times",
    rules=[
        Rule(SingleTag("00080032"), Remove()),                  # Acquisition Time
        Rule(SingleTag("00380020"), Remove()),                  # Admitting Date
        Rule(SingleTag("00380021"), Remove()),                  # Admitting Time
        Rule(SingleTag("00080033"), Remove()),                  # Content Time
        Rule(SingleTag("00080035"), Remove()),                  # Curve Time
        Rule(SingleTag("00189517"), Remove()),                  # End Acquisition DateTime
        Rule(SingleTag("00404011"), Remove()),                  # Expected Completion DateTime
        Rule(SingleTag("00340007"), Replace()),                 # Frame Origin Timestamp
        Rule(SingleTag("0016008D"), Remove()),                  # GPS Date Stamp
        Rule(SingleTag("00160077"), Remove()),                  # GPS Time Stamp
        Rule(SingleTag("00080013"), Remove()),                  # Instance Creation Time
        Rule(SingleTag("00080015"), Remove()),                  # Instance Coercion Date Time
        Rule(SingleTag("3010004D"), Remove()),                  # Intended Phase End Date
        Rule(SingleTag("3010004C"), Remove()),                  # Intended Phase Start Date
        Rule(SingleTag("30080056"), Remove()),                  # Most Recent Treatment Date
        Rule(SingleTag("0040A193"), Remove()),                  # Observation Time (Trial)
        Rule(SingleTag("00080034"), Remove()),                  # Overlay Time
        Rule(SingleTag("30080056"), Empty()),                   # Patient's Birth Date
        Rule(SingleTag("00404052"), Remove()),                  # Procedure Step Cancellation DateTime
        Rule(SingleTag("300A0007"), Remove()),                  # RT Plan Time
        Rule(SingleTag("00400004"), Remove()),                  # Scheduled Procedure Step End Date
        Rule(SingleTag("00400005"), Remove()),                  # Scheduled Procedure Step End Time
        Rule(SingleTag("00404008"), Remove()),                  # Scheduled Procedure Step Expiration DateTime
        Rule(SingleTag("00404010"), Remove()),                  # Scheduled Procedure Step Modification DateTime
        Rule(SingleTag("00400002"), Remove()),                  # Scheduled Procedure Step Start Date
        Rule(SingleTag("00404005"), Remove()),                  # Scheduled Procedure Step Start DateTime
        Rule(SingleTag("00400003"), Remove()),                  # Scheduled Procedure Step Start Time
        Rule(SingleTag("00080030"), Empty()),                   # Study Time
        Rule(SingleTag("0018936A"), Replace()),                 # Source End DateTime
        Rule(SingleTag("00080031"), Remove()),                  # Series Time
        Rule(SingleTag("30060008"), Empty()),                   # Structure Set Date
        Rule(SingleTag("30080251"), Remove()),                  # Treatment Time
        Rule(SingleTag("30060009"), Remove()),                  # Structure Set Time
        Rule(SingleTag("00400245"), Remove()),                  # Performed Procedure Step Start Time
        Rule(SingleTag("00400251"), Remove()),                  # Performed Procedure Step End Time
        Rule(SingleTag("00181201"), Remove()),                  # TimeOfLastCalibration
    ],
)
