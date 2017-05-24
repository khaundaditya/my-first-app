from django.db import models
from datetime import date
from mysite.custom_config import *
from django.core.validators import RegexValidator

# Create your models here.
class g2cServiceReport(models.Model):
	service_nm = models.CharField(max_length=150,choices=EDIST_SERVICE_NAMES)
	associated_line_department = models.CharField(max_length=20)
	delivery_channel = models.CharField(max_length=10,choices=DELIVERY_MODE)
	name_of_application = models.CharField(max_length=10,choices=OTHER_APPLICATIONS)
	is_digitally_signed = models.BooleanField(default=True)
	is_computerized = models.CharField(max_length=10,choices=WORKFLOW_MODE)
	language_of_submission = models.CharField(max_length=40)
	is_legacy_data_digitized = models.BooleanField(default=True)
	from_when = models.CharField(max_length=20)
	mode_of_storage = models.CharField(max_length=10,choices=STORAGE_MODE)
	remarks = models.CharField(max_length=100)
	district = models.CharField(max_length=30, blank=True,choices=DISTRICT_CHOICES)
	updated_date = models.CharField(max_length=10)
	user_name = models.CharField(max_length=20,default='')
	class Meta:
			 unique_together = (('service_nm', 'updated_date','district'),)
	def __str__(self):
		 return "{0} {1} {2} {3} {4} {5} {6} {7} {8} {9} {10} {12} {13} ".format( self.service_nm,self.associated_line_department,\
		 														self.delivery_channel,self.name_of_application,\
		 														self.is_digitally_signed,self.is_computerized,self.language_of_submission,self.is_legacy_data_digitized,\
		 														self.from_when,self.mode_of_storage,self.remarks,self.district,\
		 														self.updated_date,self.user_name)
class ServiceTransReport(models.Model):
	
	service_nm = models.CharField(max_length=150,choices=EDIST_SERVICE_NAMES)
	associated_line_department = models.CharField(max_length=20)
	total_transactions = models.IntegerField()
	service_charge = models.FloatField()
	statutory_charge = models.FloatField()
	total_revenue = models.FloatField()
	district = models.CharField(max_length=30, blank=True,choices=DISTRICT_CHOICES)
	updated_date = models.CharField(max_length=10)
	user_name = models.CharField(max_length=20,default='')
	class Meta:
			 unique_together = (('service_nm', 'updated_date','district'),)
	def __str__(self):
		 return "{0} {1} {2} {3} {4} {5} {6} {7} {8} ".format( self.service_nm,self.associated_line_department,self.total_transactions,\
		 														self.service_charge,self.statutory_charge,self.total_revenue,\
		 														self.district,self.updated_date,self.user_name)		 
class HardwareReport(models.Model):
	# HARDWARE_TYPES = (
 #        ('Desktop', 'Desktop'),
 #        ('Laptop', 'Laptop'),
 #        ('Printers','Printers'),
 #        ('Scanner','Scanner'),
 #        ('UPS','UPS'),
 #        ('Switch','Switch'),
 #        ('Server Computer','Server Computer')
 #    )
	#created_date = models.DateTimeField(editable=False, default=date.today,primary_key=True)
	hardware_nm = models.CharField(max_length=20,choices=HARDWARE_TYPES)
	quantity = models.IntegerField()
	status = models.CharField(max_length=60)
	hw_in_stock = models.CharField(max_length=60)
	is_amc_avaialable = models.CharField(max_length=60)
	remarks = models.CharField(max_length=100)
	district = models.CharField(max_length=30, blank=True,choices=DISTRICT_CHOICES)
	updated_date = models.CharField(max_length=10)
	user_name = models.CharField(max_length=20,default='')
	class Meta:
			 unique_together = (('hardware_nm', 'updated_date','district'),)
	def __str__(self):
		 return "{0} {1} {2} {3} {4} {5} {6} {7} {8} ".format( self.hardware_nm,self.quantity,self.status,\
		 																self.hw_in_stock,self.is_amc_avaialable,self.remarks,\
		 																self.district,self.updated_date,self.updated_date, self.user_name)
class SoftwareReport(models.Model):
	# OTHER_APPLICATIONS = (
 #        ('Dharitree', 'Dharitree'),
 #        ('ePanjeeyan', 'ePanjeeyan'),
 #        ('eSetu','eSetu'),
 #        ('CCTNS','CCTNS'),
 #        ('Vahan','Vahan')
 #    )
	#created_date = models.DateTimeField(editable=False,default=date.today,primary_key=True)
	appl_nm = models.CharField(max_length=15, choices=OTHER_APPLICATIONS)
	appl_owner = models.CharField(max_length=30)
	appl_objective = models.CharField(max_length=100)
	stakeholder_details = models.CharField(max_length=100)
	date_of_commisioning = models.CharField(max_length=12)
	name_of_application_developer = models.CharField(max_length=60)
	appl_platform_details = models.CharField(max_length=60)
	future_roadmap =  models.CharField(max_length=100)
	support_requirements = models.CharField(max_length=100)
	district = models.CharField(max_length=30, blank=True,choices=DISTRICT_CHOICES)
	updated_date = models.CharField(max_length=10)
	user_name = models.CharField(max_length=20,default='')
	class Meta:
			 unique_together = (('appl_nm', 'updated_date','district'),)
	def __str__(self):
		 return "{0} {1} {2} {3} {4} {5} {6} {7} {8} {9} {10} {11}".format( self.appl_nm,self.appl_owner,self.appl_objective,\
		 													self.stakeholder_details,self.date_of_commisioning,\
		 													self.name_of_application_developer,self.appl_platform_details,\
		 													self.future_roadmap,self.support_requirements,\
		 													self.district,self.user_name,self.updated_date)
class ManpowerReport(models.Model):
	#created_date = models.DateTimeField(editable=False,default=date.today,primary_key=True)
	person_name = models.CharField(max_length=30)
	designation = models.CharField(max_length=20)
	organization = models.CharField(max_length=40)
	work_location = models.CharField(max_length=60)
	mobile_number = models.CharField(max_length=12)
	email_id  = models.EmailField()
	district = models.CharField(max_length=30, blank=True,choices=DISTRICT_CHOICES)
	updated_date = models.CharField(max_length=10)
	user_name = models.CharField(max_length=20,default='')
	class Meta:
			 unique_together = (('person_name', 'updated_date','district'),)
	def __str__(self):
		return "{0} {1} {2} {3} {4} {5} {6} {7} {8}".format( self.person_name, self.designation,self.organization,self.work_location,\
														self.mobile_number,self.email_id,self.district,self.updated_date,self.user_name)
class CSCReport(models.Model):
	# CONNECTIVITY_MODES = (
 #        ('B', 'Broadband'),
 #        ('3G', '3G Dongle'),
 #        ('4G','4G Dongle')
 #    )
	alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')
	#created_date = models.DateTimeField(editable=False,default=date.today,primary_key=True)
	omt_id =  models.CharField(max_length=50, blank=True, null=True, validators=[alphanumeric])
	vle_name = models.CharField(max_length=50, blank=True, null=True)
	gaon_panchayat_name = models.CharField(max_length=100, blank=True, null=True)
	address = models.CharField(max_length=100, blank=True, null=True)
	mobile_number = models.CharField(max_length=12)
	infra_details = models.CharField(max_length=100, blank=True, null=True)
	connectivity_modes = models.CharField(max_length=2, choices=CONNECTIVITY_MODES)
	num_g2c_and_g2g_services = models.IntegerField()
	num_g2b_and_other_services = models.IntegerField()
	remarks = models.CharField(max_length=100, blank=True, null=True)
	district = models.CharField(max_length=30, blank=True,choices=DISTRICT_CHOICES)
	updated_date = models.CharField(max_length=10)
	user_name = models.CharField(max_length=20,default='')
	class Meta:
			 unique_together = (('omt_id', 'updated_date','district'),)
	def __str__(self):
		return "{0} {1} {2} {3} {4} {5} {6} {7} {8} {9} {10} {11} {12}".format( self.omt_id, self.vle_name,self.gaon_panchayat_name,self.address,\
														self.mobile_number,self.infra_details,self.connectivity_modes,self.num_g2c_and_g2g_services,\
														self.num_g2b_and_other_services,self.remarks,self.district,self.updated_date,self.user_name
														)

class SWANReport(models.Model):
	# CONNECTIVITY_TYPES = (
 #        ('UTP', 'UTP'),
 #        ('WiFi', 'WiFi'),
 #        ('OFC','Optical Fibre')
 #    )
	#created_date = models.DateTimeField(editable=False,default=date.today,primary_key=True)
	pop_names =  models.CharField(max_length=50, blank=True, null=True)
	distance_from_hq = models.CharField(max_length=10, blank=True, null=True)
	offices_connected_with_pop = models.CharField(max_length=100, blank=True, null=True)
	distance_from_pop =  models.CharField(max_length=100, blank=True, null=True)
	connectivity_types = models.CharField(max_length=4, choices=CONNECTIVITY_TYPES)
	internet_bandwidth = models.CharField(max_length=50, blank=True, null=True)
	is_functional = models.BooleanField(default=False)
	when_last_up = models.CharField(max_length=15, blank=True, null=True)
	pop_manpower = models.CharField(max_length=50, blank=True, null=True)
	reasons_for_not_working = models.CharField(max_length=50, blank=True, null=True,default='NA')
	remarks = models.CharField(max_length=100, blank=True, null=True)
	district = models.CharField(max_length=30, blank=True,choices=DISTRICT_CHOICES)
	updated_date = models.CharField(max_length=10)
	user_name = models.CharField(max_length=20,default='')
	class Meta:
			 unique_together = (('pop_names', 'updated_date','district'),)
	def __str__(self):
		return "{0} {1} {2} {3} {4} {5} {6} {7} {8} {9} {10} {11} {12} {13}".format(self.pop_names,self.distance_from_hq,self.offices_connected_with_pop,\
																			self.distance_from_pop,self.connectivity_types,self.internet_bandwidth,self.is_functional,\
																			self.when_last_up,self.pop_manpower,self.reasons_for_not_working,self.remarks,self.district,\
																			self.updated_date,self.user_name

																			)

class DLReport(models.Model):
	#created_date = models.DateTimeField(editable=False,default=date.today,primary_key=True)
	lac_name = models.CharField(max_length=50, blank=True, null=True)
	num_training_centres = models.IntegerField()
	num_examination_centres_near_gp = models.CharField(max_length=100, blank=True, null=True)
	num_beneficiaries_registered =  models.IntegerField()
	num_beneficiaries_under_training =  models.IntegerField()
	num_beneficiaries_trained =  models.IntegerField()
	num_beneficiaries_appeared_in_exam =  models.IntegerField()
	num_beneficiaries_passed_in_exam =  models.IntegerField()
	district = models.CharField(max_length=30, blank=True,choices=DISTRICT_CHOICES)
	updated_date = models.CharField(max_length=10)
	user_name = models.CharField(max_length=20,default='')
	class Meta:
			 unique_together = (('lac_name', 'updated_date','district'),)
	def __str__(self):
		return "{0} {1} {2} {3} {4} {5} {6} {7} {8} {9} {10}".format(self.lac_names,self.num_training_centres,self.num_examination_centres_near_gp,\
															self.num_beneficiaries_registered,self.num_beneficiaries_under_training,\
															self.num_beneficiaries_trained,self.num_beneficiaries_appeared_in_exam,\
															self.num_beneficiaries_passed_in_exam,self.district,self.updated_date,self.user_name)

class NOFNReport(models.Model):
	# MY_CHOICE = (
 #        ('GP', 'GP'),
 #        ('Block', 'Block'),
 #    )
	#created_date = models.DateTimeField(editable=False,default=date.today,primary_key=True)
	gp_name = models.CharField(max_length=50, blank=True, null=True)
	block_name = models.CharField(max_length=50, blank=True, null=True)
	is_fibre_layered_upto_gp = models.BooleanField(default=False)
	is_gpon_installed_at_block =  models.BooleanField(default=True)
	is_gpon_termination_done_at_GP =  models.BooleanField(default=True)
	nofn_pop_build_at =  models.CharField(max_length=4, choices=NOFN_CHOICE)
	is_network_access_available_at_village = models.BooleanField(default=True)
	remarks = models.CharField(max_length=100, blank=True, null=True)
	district = models.CharField(max_length=30, blank=True,choices=DISTRICT_CHOICES)
	updated_date = models.CharField(max_length=10)
	user_name = models.CharField(max_length=20,default='')
	class Meta:
			 unique_together = (('gp_name', 'updated_date','district'),)
	def __str__(self):
		return "{0} {1} {2} {3} {4} {5} {6} {7} {8} {9} {10} {11}".format(self.gp_name,self.block_name,self.is_fibre_layered_upto_gp,\
															self.is_gpon_installed_at_block,self.is_gpon_termination_done_at_GP,\
															self.nofn_pop_build_at,self.is_network_access_available_at_village,\
															self.remarks,self.district,self.updated_date,self.user_name)
