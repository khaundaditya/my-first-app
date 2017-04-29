DISTRICT_CHOICES = (

		('BK','Baksa'),
		('BP','Barpeta'),
		('BS','Biswanath'),
		('BO','Bongaigaon'),
		('CA','Cachar'),
		('CD','Charaideo'),
		('CH','Chirang'),
		('DR','Darrang'),
		('DM','Dhemaji'),
		('DU','Dhubri'),
		('DI','Dibrugarh'),
		('GP','Goalpara'),
		('GG','Golaghat'),
		('HA','Hailakandi'),
		('HJ','Hojai'),
		('JO','Jorhat'),
		('KM','Kamrup Metropolitan'),
		('KU','Kamrup'),
		('KG','Karbi Anglong'),
		('KR','Karimganj'),
		('KJ','Kokrajhar'),
		('LA','Lakhimpur'),
		('MJ','Majuli'),
		('MA','Morigaon'),
		('NN','Nagaon'),
		('NB','Nalbari'),
		('NC','Dima Hasao'),
		('SV','Sivasagar'),
		('ST','Sonitpur'),
		('SM','South Salmara-Mankachar'),
		('TI','Tinsukia'),
		('UD','Udalguri'),
		('WK','West Karbi Anglong')
)
EDIST_SERVICE_NAMES = (
		('Next of Kin certificate','Next of Kin certificate'), 
		('Senior Citizen Certificate','Senior Citizen Certificate'), 
		('Delayed Birth Permission','Delayed Birth Permission'), 
		('Delayed Death Permission','Delayed Death Permission'), 
		('Issuance of Birth Certificate','Issuance of Birth Certificate'), 
		('Issuance of Death Certificate','Issuance of Death Certificate'), 
		('Permanent Resident Certificate','Permanent Resident Certificate'), 
		('Renewal of Explosive License','Renewal of Explosive License'), 
		('Permission for Special Events u/s 144 CrPC','Permission for Special Events u/s 144 CrPC'), 
		('Permission for Fairs/Religious/ Cultural Festivals/Loud Speakers/ Rallies/Strikes','Permission for Fairs/Religious/ Cultural Festivals/Loud Speakers/ Rallies/Strikes'), 
		('Income Certificate','Income Certificate'), 
		('Bakijai Clearance Certificate','Bakijai Clearance Certificate'), 
		('Application for Court Marriage','Application for Court Marriage'), 
		('Application for Marriage Certificate','Application for Marriage Certificate'), 
		('Application for Stamp Vendor License','Application for Stamp Vendor License'), 
		('Submission of Application for Mutation','Submission of Application for Mutation'), 
		('Certified Copy of Mutation Order','Certified Copy of Mutation Order'), 
		('Issue of Land Valuation Certificate','Issue of Land Valuation Certificate'), 
		('Issue of Record of Rights (Jamabandi)','Issue of Record of Rights (Jamabandi)'), 
		('Issue of Non Encumbrance Certificate','Issue of Non Encumbrance Certificate'), 
		('Issue of Land Holding Certificate','Issue of Land Holding Certificate'), 
		('Application for Registration of Deeds, etc.','Application for Registration of Deeds, etc.'), 
		('Permission for Transfer of Property by way of Mortgage, Lease, Gift, Sale, etc.','Permission for Transfer of Property by way of Mortgage, Lease, Gift, Sale, etc.'), 
		('Assessment of Stamp Duty and Registration Fees','Assessment of Stamp Duty and Registration Fees'), 
		('Certified Copies of cause list, judgements, etc','Certified Copies of cause list, judgements, etc'), 
		('Registration of name in employment exchange','Registration of name in employment exchange'), 
		('Application for change of name/ address/ age in employment exchange','Application for change of name/ address/ age in employment exchange'), 
		('Application for transfer of enrollment to other district employment exchange','Application for transfer of enrollment to other district employment exchange'), 
		('Surrender of Employment Exchange Card','Surrender of Employment Exchange Card'), 
		('Issue of Duplicate Mark sheet','Issue of Duplicate Mark sheet'), 
		('Issue of Duplicate Pass Certificate','Issue of Duplicate Pass Certificate'), 
		('Issue of Migration Certificate','Issue of Migration Certificate'), 
		('Issue of Duplicate Mark sheet','Issue of Duplicate Mark sheet'), 
		('Issue of Duplicate Pass Certificate','Issue of Duplicate Pass Certificate'), 
		('Issue of Migration Certificate','Issue of Migration Certificate'), 
		('Non-Creamy layer Certificate','Non-Creamy layer Certificate'), 
		('Caste Certificate for SC','Caste Certificate for SC'), 
		('Application for Driving License','Application for Driving License'), 
		('Application for Renewal of Driving License','Application for Renewal of Driving License'), 
		('Application for Learners License','Application for Learners License'), 
		('Application for Driving Test','Application for Driving Test'), 
		('Application for grant of Fresh License to sell stock etc','Application for grant of Fresh License to sell stock etc'), 
		('Application for grant of Renewal of License to sell stock etc','Application for grant of Renewal of License to sell stock etc'), 
		('Application for Information under RTI','Application for Information under RTI'), 
		('RTI Appeal','RTI Appeal'), 
		('Certified Copy of Electoral Roll','Certified Copy of Electoral Roll'), 

 )
HARDWARE_TYPES = (
        ('Desktop', 'Desktop'),
        ('Laptop', 'Laptop'),
        ('Printers','Printers'),
        ('Scanner','Scanner'),
        ('UPS','UPS'),
        ('Switch','Switch'),
        ('Server Computer','Server Computer')
  )
OTHER_APPLICATIONS = (
        ('Dharitree', 'Dharitree'),
        ('ePanjeeyan', 'ePanjeeyan'),
        ('eSetu','eSetu'),
        ('CCTNS','CCTNS'),
        ('Vahan','Vahan'),
        ('eDistrict','eDistrict')
    )
CONNECTIVITY_MODES = (
        ('B', 'Broadband'),
        ('3G', '3G Dongle'),
        ('4G','4G Dongle')
    )
CONNECTIVITY_TYPES = (
        ('UTP', 'UTP'),
        ('WiFi', 'WiFi'),
        ('OFC','Optical Fibre')
    )
NOFN_CHOICE = (
        ('GP', 'GP'),
        ('Block', 'Block'),
    )
DELIVERY_MODE = (
        ('Online', 'Online'),
        ('Offline', 'Offline'),
    )
REPORT_NAMES = (

	('-------', '--------'),
   ('Manpower', 'Manpower Report'),
   ('CSC', 'CSC Report'), 
   ('Hardware', 'Hardware Report'),
   ('Software', 'Software Report'),
   ('SWAN', 'SWAN Report'),
   ('NOFN', 'NOFN Report'),
   ('DigitalLiteracy', 'Digital Literacy Report'),
   ('eDistrictTrans','e-District Transaction Report'),
   ('G2CServices','G2C Services Report')


)
WORKFLOW_MODE = (

	 ('Yes', 'Yes'),
     ('No', 'No'),
     ('Partially', 'Partially'),

)
STORAGE_MODE = (

	 ('Local', 'Local'),
     ('Centralized', 'Centralized'),
     

)
LANGUAGE_CHOICES = (

	 ('Assamese', 'Assamese'),
     ('English', 'English'),
     ('Bengali', 'Bengali'),
     ('Bodo', 'Bodo'),
     

)
SERVICE_TO_DEPARTMENT_MAP = {

	'Next of Kin certificate': 'GAD',
	'Senior Citizen Certificate': 'GAD',
	'Delayed Birth Permission': 'Health/ UDD/ GMDA',
	'Delayed Death Permission': 'Health/ UDD/ GMDA',
	'Issuance of Birth Certificate': 'Health/ UDD/ GMDA',
	'Issuance of Death Certificate': 'Health/ UDD/ GMDA',
	'Permanent Resident Certificate': 'Home & Political',
	'Renewal of Explosive License': 'Home & Political',
	'Permission for Special Events u/s 144 CrPC': 'Home & Political',
	'Permission for Fairs/Religious/ Cultural Festivals/Loud Speakers/ Rallies/Strikes': 'Home & Political',
	'Income Certificate': 'Revenue',
	'Bakijai Clearance Certificate': 'Revenue',
	'Application for Court Marriage': 'Revenue',
	'Application for Marriage Certificate': 'Revenue',
	'Application for Stamp Vendor License': 'Revenue',
	'Submission of Application for Mutation': 'Revenue',
	'Certified Copy of Mutation Order': 'Revenue',
	'Issue of Land Valuation Certificate': 'Revenue',
	'Issue of Record of Rights (Jamabandi)': 'Revenue',
	'Issue of Non Encumbrance Certificate': 'Revenue',
	'Issue of Land Holding Certificate': 'Revenue',
	'Permission for Transfer of Property by way of Mortgage, Lease, Gift, Sale, etc.': 'Revenue',
	'Assessment of Stamp Duty and Registration Fees': 'Revenue',
	'Certified Copies of cause list, judgements, etc': 'Revenue',
	'Registration of name in employment exchange': 'Labour & Employment',
	'Application for change of name/ address/ age in employment exchange': 'Labour & Employment',
	'Application for transfer of enrollment to other district employment exchange': 'Labour & Employment',
	'Surrender of Employment Exchange Card': 'Labour & Employment',
	'Issue of Duplicate Mark sheet': 'AHSEC',
	'Issue of Duplicate Pass Certificate': 'AHSEC',
	'Issue of Migration Certificate': 'AHSEC',
	'Issue of Duplicate Mark sheet': 'Board of Secondary Education',
	'Issue of Duplicate Pass Certificate': 'Board of Secondary Education',
	'Issue of Migration Certificate': 'Board of Secondary Education',
	'Non-Creamy layer Certificate': 'WPT&BC',
	'Caste Certificate for SC': 'WPT&BC',
	'Application for Driving License': 'Transport',
	'Application for Renewal of Driving License': 'Transport',
	'Application for Learners License': 'Transport',
	'Application for Driving Test': 'Transport',
	'Application for grant of Fresh License to sell stock etc': 'Agriculture Department',
	'Application for grant of Renewal of License to sell stock etc': 'Agriculture Department',
	'Application for Information under RTI': 'ART',
	'RTI Appeal': 'ART',
	'Certified Copy of Electoral Roll': 'Election'
	
}