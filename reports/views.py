from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from django.contrib import messages
from django.forms.formsets import formset_factory
from django.template import RequestContext
from django.template.loader import render_to_string
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.db.models import Q
from django.contrib import messages
from django.conf import settings
import os
import re

from .forms import *
#from .models import HardwareReport,ManpowerReport,CSCReport,HardwareReport,SWANReport,DigitalLiteracyReport,NOFNReport,SoftwareReport
from django.contrib.auth.decorators import login_required
from reviewer.models import *
from .models import *
from mysite import custom_config
#from .models import HardwareReport
# Create your views here.
district_dict = dict(DISTRICT_CHOICES)
@login_required
def generateHardwareReport(request):
	HardNormSet = formset_factory(HardwareReportForm,extra=2)
	context = {}
	if request.method == 'POST':
		formset = HardNormSet(request.POST)
		try:
			if formset.is_valid():
				com_dist = ''
				for form in formset:
					
					cd = form.cleaned_data
					dist = cd['district']
					if not dist:
						dist = com_dist
					else:
						com_dist = dist
					timestamp  = timezone.now()
					today_date=timestamp.strftime('%Y%m%d')
					YYYYMM = timestamp.strftime('%Y%m')
					district_full_name = district_dict[dist]
					hw_db_obj = HardwareReport( hardware_nm=cd['hardware_nm'],\
										quantity = cd['quantity'],status=cd['status'],\
										hw_in_stock = str(cd['hw_in_stock']),is_amc_avaialable=cd['is_amc_avaialable'],\
										remarks=cd['remarks'],district=dist,updated_date=today_date,user_name=request.user)
					print(cd)	
					try:
						if _isReportInProgress(dist,request.user,'Software'):
							msg = "your previous submission for Hardware  report hasn't yet be closed.New data willn't be saved"
							messages.warning(request, msg)
							print(msg)
						else:							
							hw_db_obj.save()
							
					except IntegrityError:
						msg = 'Similar set of data already submitted today.Hence can\'t be re-submitted'
						messages.error(request, msg)
				saved_snapshot =_updateSnapshotData(request.user,'Hardware',YYYYMM,dist)
				return render(request,'reports/csc_submission.html',{'form':form})
			else:
				print "FormSet is not valid"
				print formset.errors	
			
		except ValidationError:
			formset = None
	else:

		context = {'formset': HardNormSet()}
	return render(request,'reports/hardware.html',context)	

@login_required
def generateSoftwareReport(request):
	SoftNormSet = formset_factory(SoftwareReportForm,extra=2)
	context = {}
	if request.method == 'POST':
		#form = ManpowerReportForm(request.POST)
		formset = SoftNormSet(request.POST)
		try:
			if formset.is_valid():
				for form in formset:
					com_dist = ''
					cd = form.cleaned_data
					dist = cd['district']
					if not dist:
						dist = com_dist
					else:
						com_dist = dist
					timestamp  = timezone.now()
					today_date=timestamp.strftime('%Y%m%d')
					YYYYMM = timestamp.strftime('%Y%m')
					sw_db_obj = SoftwareReport( appl_owner=cd['appl_owner'],appl_objective=cd['appl_objective'],\
						stakeholder_details=cd['stakeholder_details'],date_of_commisioning=cd['date_of_commisioning'],\
						name_of_application_developer=cd['name_of_application_developer'],\
						appl_platform_details=cd['appl_platform_details'],\
						future_roadmap=cd['future_roadmap'],support_requirements=cd['support_requirements'],updated_date=today_date,district=dist,user_name=request.user)
					print(cd)	
					try:
						if _isReportInProgress(dist,request.user,'Software'):
							msg = "your previous submission for Software  report hasn't yet be closed.New data willn't be saved"
							messages.warning(request, msg)
							print(msg)
						else:							
							sw_db_obj.save()
							
					except IntegrityError:
						msg = 'Similar set of data already submitted today.Hence can\'t be re-submitted'
						messages.error(request, msg)	
					saved_snapshot =_updateSnapshotData(request.user,'Software',YYYYMM,dist)
					return render(request,'reports/csc_submission.html',{'form':form})

				return render(request,'reports/csc_submission.html',{'form':form})
			else:
				print "FormSet is not valid"
				print formset.errors	
		except ValidationError:
			formset = None
	else:
		#form =  ManpowerReportForm()
		#context = {'formset': ManpowerFormSet(),'loop_times': range(1,3)}
		context = {'formset': SoftNormSet(),'report_name': 'Software Report'}
	return render(request,'reports/software.html',context)	

@login_required
def generateNOFNeport(request):
	NOFNormSet = formset_factory(NOFNReportForm,extra=2)
	context = {}
	if request.method == 'POST':
		#form = ManpowerReportForm(request.POST)
		formset = NOFNormSet(request.POST)
		try:
			if formset.is_valid():
				com_dist = ''
				for form in formset:
					
					cd = form.cleaned_data
					dist = cd['district']
					if not dist:
						dist = com_dist
					else:
						com_dist = dist
					timestamp  = timezone.now()
					today_date=timestamp.strftime('%Y%m%d')
					YYYYMM = timestamp.strftime('%Y%m')
					nfn_db_obj = NOFNReport( gp_name=cd['gp_name'],block_name=cd['block_name'],is_fibre_layered_upto_gp=cd['is_fibre_layered_upto_gp'],\
										is_gpon_installed_at_block=cd['is_gpon_installed_at_block'],\
										is_gpon_termination_done_at_GP=cd['is_gpon_termination_done_at_GP'],nofn_pop_build_at=cd['nofn_pop_build_at'],\
										is_network_access_available_at_village=cd['is_network_access_available_at_village'],\
										remarks=cd['remarks'],updated_date=today_date,district=dist,user_name=request.user)
					print(cd)	
					try:
						if _isReportInProgress(dist,request.user,'NOFN'):
							msg = "your previous submission for NOFN  report hasn't yet be closed.New data willn't be saved"
							messages.warning(request, msg)
							print(msg)
						else:							
							nfn_db_obj.save()
							
					except IntegrityError:
						msg = 'Similar set of data already submitted today.Hence can\'t be re-submitted'
						messages.error(request, msg)

				saved_snapshot =_updateSnapshotData(request.user,'NOFN',YYYYMM,dist)
				return render(request,'reports/csc_submission.html',{'form':form})
			else:
				print "FormSet is not valid"
				print formset.errors
		except ValidationError:
			formset = None
	else:
		#form =  ManpowerReportForm()
		#context = {'formset': ManpowerFormSet(),'loop_times': range(1,3)}
		context = {'formset': NOFNormSet()}
	return render(request,'reports/nofn.html',context)	


@login_required
def generateDLReport(request):
	DLFormSet = formset_factory(DigitalLiteracyReportForm,extra=2)
	context = {}
	if request.method == 'POST':
		formset = DLFormSet(request.POST)
		try:
			if formset.is_valid():
				com_dist = ''
				for form in formset:
					
					cd = form.cleaned_data
					dist = cd['district']
					if not dist:
						dist = com_dist
					else:
						com_dist = dist
					timestamp  = timezone.now()
					today_date=timestamp.strftime('%Y%m%d')
					YYYYMM = timestamp.strftime('%Y%m')
					dl_db_obj = DLReport( lac_name=cd['lac_name'],\
						num_training_centres=cd['num_training_centres'],num_examination_centres_near_gp=cd['num_examination_centres_near_gp'],\
						num_beneficiaries_registered = cd['num_beneficiaries_registered'],num_beneficiaries_under_training=cd['num_beneficiaries_under_training'],num_beneficiaries_trained=cd['num_beneficiaries_trained'],num_beneficiaries_appeared_in_exam=cd['num_beneficiaries_appeared_in_exam'],\
						num_beneficiaries_passed_in_exam=cd['num_beneficiaries_passed_in_exam'],updated_date=today_date,district=dist,user_name=request.user)
					print(cd)
					#form.save()
					try:
						if _isReportInProgress(dist,request.user,'DigitalLiteracy'):
							msg = "your previous submission for Digital Literacy  report hasn't yet be closed.New data willn't be saved"
							messages.warning(request, msg)
							print(msg)
						else:
							print "Going to save Object"							
							dl_db_obj.save()
							
					except IntegrityError:
						msg = 'Similar set of data already submitted today.Hence can\'t be re-submitted'
						messages.error(request, msg)
						#return HttpResponse("ERROR: Data already exists!")	
				saved_snapshot =_updateSnapshotData(request.user,'DigitalLiteracy',YYYYMM,dist)
				return render(request,'reports/csc_submission.html',{'form':form})
				
			else:
				print "FormSet is not valid"
				print formset.errors
		except ValidationError:
			formset = None
	else:
		#form =  ManpowerReportForm()
		#context = {'formset': ManpowerFormSet(),'loop_times': range(1,3)}
		context = {'formset': DLFormSet()}
	return render(request,'reports/digital_literacy.html',context)	
@login_required
def generateSWANReport(request):
	SWANFormSet = formset_factory(SWANReportForm,extra=2)
	context = {}
	if request.method == 'POST':
		#form = ManpowerReportForm(request.POST)
		formset = SWANFormSet(request.POST)
		try:
			if formset.is_valid():
				com_dist = ''
				for form in formset:
					cd = form.cleaned_data
					dist = cd['district']
					if not dist:
						dist = com_dist
					else:
						com_dist = dist
					timestamp  = timezone.now()
					today_date=timestamp.strftime('%Y%m%d')
					YYYYMM = timestamp.strftime('%Y%m')
					swan_db_obj = SWANReport( pop_names=cd['pop_names'],\
						distance_from_hq=cd['distance_from_hq'],offices_connected_with_pop=cd['offices_connected_with_pop'],distance_from_pop=cd['distance_from_pop'],\
						connectivity_types=cd['connectivity_types'],internet_bandwidth=cd['internet_bandwidth'],is_functional=cd['is_functional'],\
						when_last_up=cd['when_last_up'],pop_manpower=cd['pop_manpower'],\
						reasons_for_not_working=cd['reasons_for_not_working'], remarks=cd['remarks'],updated_date=today_date,district=dist,user_name=request.user)
					print(cd)	
					try:
						if _isReportInProgress(dist,request.user,'SWAN'):
							msg = "your previous submission for SWAN  report hasn't yet be closed.New data willn't be saved"
							messages.warning(request, msg)
							print(msg)
						else:							
							swan_db_obj.save()
							
					except IntegrityError:
						msg = 'Similar set of data already submitted today.Hence can\'t be re-submitted'
						messages.error(request, msg)	
				saved_snapshot =_updateSnapshotData(request.user,'SWAN',YYYYMM,dist)
				return render(request,'reports/csc_submission.html',{'form':form})
		except ValidationError:
			formset = None
	else:
		#form =  ManpowerReportForm()
		#context = {'formset': ManpowerFormSet(),'loop_times': range(1,3)}
		context = {'formset': SWANFormSet()}
	return render(request,'reports/swan.html',context)

@login_required
def generateCSCReport(request):
	CSCFormSet = formset_factory(CSCReportForm,extra=2)
	context = {}
	if request.method == 'POST':
		formset = CSCFormSet(request.POST)
		try:
			if formset.is_valid():
				com_dist = ''
				for form in formset:
					
					cd = form.cleaned_data
					dist = cd['district']
					if not dist:
						dist = com_dist
					else:
						com_dist = dist
					timestamp  = timezone.now()	
					today_date=_getTodayDate()	
					YYYYMM = timestamp.strftime('%Y%m')					
					csc = CSCReport( omt_id=cd['omt_id'],\
						vle_name=cd['vle_name'],gaon_panchayat_name=cd['gaon_panchayat_name'],address=cd['address'],\
						mobile_number=cd['mobile_number'],infra_details=cd['infra_details'],connectivity_modes=cd['connectivity_modes'],\
						num_g2c_and_g2g_services=cd['num_g2c_and_g2g_services'],num_g2b_and_other_services=cd['num_g2b_and_other_services'],\
						 remarks=cd['remarks'],district=dist,updated_date=today_date,user_name=request.user)
					print(cd)	
					#form.save()
					try:
						#csc.save()

						if _isReportInProgress(dist,request.user,'CSC'):
							msg = "your previous submission for CSC  report hasn't yet be closed.New data willn't be saved"
							messages.warning(request, msg)
							print(msg)
						else:							
							csc.save()
							
					except IntegrityError:
						msg = 'Similar set of data already submitted today.Hence can\'t be re-submitted'
						messages.error(request, msg)
				saved_snapshot = _updateSnapshotData(request.user,'CSC',YYYYMM,dist)
				return render(request,'reports/csc_submission.html',{'form':form})
			else:
				print formset.errors
		except ValidationError:
			formset = None
	else:
		#form =  ManpowerReportForm()
		#context = {'formset': ManpowerFormSet(),'loop_times': range(1,3)}
		context = {'formset': CSCFormSet()}
	return render(request,'reports/csc.html',context)

@login_required
def generateManpowerReport(request):

	ManpowerFormSet = formset_factory(ManpowerReportForm,extra=2)
	context = {}
	if request.method == 'POST':
		#form = ManpowerReportForm(request.POST)
		today_date = ''
		formset = ManpowerFormSet(request.POST)
		try:
			if formset.is_valid():
				com_dist = ''
				for form in formset:
					
					cd = form.cleaned_data
					dist = cd['district']
					if not dist:
						dist = com_dist
					else:
						com_dist = dist
					timestamp  = timezone.now()
					today_date=timestamp.strftime('%Y%m%d')
					YYYYMM = timestamp.strftime('%Y%m')
					manpower = ManpowerReport( person_name=cd['person_name'],\
						designation=cd['designation'] ,organization=cd['organization'],work_location=cd['work_location'],
						mobile_number = cd['mobile_number'],email_id = cd['email_id'],district=dist,updated_date=today_date,user_name=request.user
						)	
					#form.save()
					try:
						if _isReportInProgress(dist,request.user,'Manpower'):
							msg = "your previous submission for Manpower  report hasn't yet be closed.New data willn't be saved"
							messages.warning(request, msg)
							print(msg)
						else:							
							manpower.save()
							
					except IntegrityError:
						msg = 'Similar set of data already submitted today.Hence can\'t be re-submitted'
						messages.error(request, msg)
				saved_snapshot =_updateSnapshotData(request.user,'Manpower',YYYYMM,dist)

				return render(request,'reports/csc_submission.html',{'form':form})
			else:
				print "FormSet is not valid"
				print formset.errors
		except ValidationError:
			formset = None
	else:
		#form =  ManpowerReportForm()
		#context = {'formset': ManpowerFormSet(),'loop_times': range(1,3)}

		context = {'formset': ManpowerFormSet()}

	return render(request,'reports/manpower.html',context)
	#return render(request, 'reports/reports.html', {'HardwareReport': HardwareReport.objects.all()})

@login_required
def generateG2CServiceReport(request):

	G2CServiceFormSet = formset_factory(G2CServiceReportForm,extra=3)
	context = {}
	if request.method == 'POST':
		#form = ManpowerReportForm(request.POST)
		today_date = ''
		formset = G2CServiceFormSet(request.POST)
		try:
			if formset.is_valid():
				com_dist = ''
				for form in formset:
					
					cd = form.cleaned_data
					dist = cd['district']
					if not dist:
						dist = com_dist
					else:
						com_dist = dist
					timestamp  = timezone.now()
					today_date=timestamp.strftime('%Y%m%d')
					YYYYMM = timestamp.strftime('%Y%m')
					department = SERVICE_TO_DEPARTMENT_MAP[cd['service_nm']]
					g2c_db_obj = g2cServiceReport(service_nm = cd['service_nm'],associated_line_department=department,\
						delivery_channel = cd['delivery_channel'],name_of_application=cd['name_of_application'],\
						is_digitally_signed=cd['is_digitally_signed'],is_computerized=cd['is_computerized'],\
						from_when=cd['from_when'],mode_of_storage=cd['mode_of_storage'],remarks=cd['mode_of_storage'],\
						district=dist,updated_date=today_date,user_name=request.user)

					try:
						if _isReportInProgress(dist,request.user,'G2CServices'):
							msg = "your previous submission for G2C Services  report hasn't yet be closed.New data willn't be saved"
							messages.warning(request, msg)
							print(msg)
						else:							
							g2c_db_obj.save()
							
					except IntegrityError:
						msg = 'Similar set of data already submitted today.Hence can\'t be re-submitted'
						messages.error(request, msg)
				saved_snapshot =_updateSnapshotData(request.user,'G2CServices',YYYYMM,dist)

				return render(request,'reports/csc_submission.html',{"form":form})
			else:
				print "FormSet is not valid"
				print formset.errors
		except ValidationError:
			formset = None
	else:
		#form =  ManpowerReportForm()
		#context = {'formset': ManpowerFormSet(),'loop_times': range(1,3)}

		context = {'formset': G2CServiceFormSet() }

	return render(request,'reports/g2c_service.html',context)
	#return render(request, 'reports/reports.html', {'HardwareReport': HardwareReport.objects.all()})

@login_required
def generateeDistrictTransactionReport(request):

	eDistTransFormSet = formset_factory(eDistrictReportForm,extra=3)
	context = {}
	if request.method == 'POST':
		#form = ManpowerReportForm(request.POST)
		today_date = ''
		formset = eDistTransFormSet(request.POST)
		try:
			if formset.is_valid():
				com_dist = ''
				for form in formset:
					
					cd = form.cleaned_data
					dist = cd['district']
					if not dist:
						dist = com_dist
					else:
						com_dist = dist
					timestamp  = timezone.now()
					today_date=timestamp.strftime('%Y%m%d')
					YYYYMM = timestamp.strftime('%Y%m')

					department = SERVICE_TO_DEPARTMENT_MAP[cd['service_nm']]
					edist_db_object = ServiceTransReport( service_nm=cd['service_nm'],\
						associated_line_department=department ,total_transactions=cd['total_transactions'],service_charge=cd['service_charge'],statutory_charge=cd['statutory_charge'],
						total_revenue = cd['total_revenue'],district = dist,updated_date=today_date,user_name=request.user
						)	
					#form.save()
					print(cd)
					try:
						if _isReportInProgress(dist,request.user,'eDistrictTrans'):
							msg = "your previous submission for eDistrict Transaction  report hasn't yet be closed.New data willn't be saved"
							messages.warning(request, msg)
							print(msg)
						else:						
							edist_db_object.save()
							
					except IntegrityError:
						msg = 'Similar set of data already submitted today.Hence can\'t be re-submitted'
						messages.error(request, msg)
				saved_snapshot =_updateSnapshotData(request.user,'eDistrictTrans',YYYYMM,dist)

				return render(request,'reports/csc_submission.html',{"form":form})
			else:
				print "FormSet is not valid"
				print formset.errors
		except ValidationError:
			formset = None
	else:
		#form =  ManpowerReportForm()
		#context = {'formset': ManpowerFormSet(),'loop_times': range(1,3)}

		context = {'formset': eDistTransFormSet() }

	return render(request,'reports/edistrict_transaction.html',context)
	#return render(request, 'reports/reports.html', {'HardwareReport': HardwareReport.objects.all()})

@login_required
def updateManpowerReport(request):
	return HttpResponse('true')



"""
Private Helper Routines
"""
def _getSpecficModelQuerySet(report_name):
	if report_name == 'Manpower':
		return  ManpowerReport.objects.all()
	elif report_name == 'CSC':
		return  CSCReport.objects.all()
	elif report_name == 'Hardware':
		return  HardwareReport.objects.all()
	elif report_name == 'Software':
		return  SoftwareReport.objects.all()
	elif report_name == 'SWAN':
		return  SWANReport.objects.all()
	elif report_name == 'NOFN':
		return  NOFNReport.objects.all()
	elif report_name == 'DigitalLiteracy':
		return  DLReport.objects.all()
	elif report_name == 'G2CServices':
		return  g2cServiceReport.objects.all()
	elif report_name == 'eDistrictTrans':
		return  ServiceTransReport.objects.all()

def _updateSnapshotData(user,report_name,YYYYMM,district):
	queryset = _getSpecficModelQuerySet(report_name)
	district_full_name = district_dict[district]

	filtered_result = _getFilteredResult(queryset,district,YYYYMM)
	context = {'filtered_result': filtered_result,\
	'report_name': report_name,'district': district,'YYYYMM':YYYYMM,'include_href':1,\
	'district_full_name':district_full_name,'override' : 1 }
	templ_name = _getTemplateFile(report_name)
	content = render_to_string(templ_name, context)
	print(content)
	bin_content = _convertStringToByte(content)
	obj = ReportSnapShot.objects.filter(district=district,report_type=report_name,owner=user)
	if obj.exists():
		print("Updating Existing Snapshot")
		obj.content = b''
		obj.update(content=bin_content)
	else:
		Snapshot = ReportSnapShot(content=bin_content,owner=user,report_type=report_name,district=district,state='submitted',YYYYMM=YYYYMM)
		#try:
		Snapshot.save()

		#except IntegrityError:
		#	msg = "Data Aleady Exists for this " + report_name + " reportss!"
			#messages.warning(msg)
		#	print(msg)
	return filtered_result		
def _getTemplateFile(report_name):
	TEMPL_DIR = os.path.abspath(os.path.join(settings.PROJECT_DIR,'../reviewer/templates/reviewer'))
	templ_name = ''
	if report_name == 'Manpower':
		templ_name = TEMPL_DIR + '/mp.html'
	elif report_name == 'CSC':
		templ_name = TEMPL_DIR + '/csc.html'
	elif report_name == 'SWAN':
		templ_name = TEMPL_DIR + '/swan.html'
	elif report_name == 'NOFN':
		templ_name = TEMPL_DIR + '/nofn.html'
	elif report_name == '':
		templ_name = TEMPL_DIR + '/swan.html'
	elif report_name == 'Hardware':
		templ_name = TEMPL_DIR + '/hardware.html'
	elif report_name == 'Software':
		templ_name = TEMPL_DIR + '/software.html'
	elif report_name == 'DigitalLiteracy':
		templ_name = TEMPL_DIR + '/digital_literacy.html'
	elif report_name == 'eDistrictTrans':
		templ_name = TEMPL_DIR + '/edistrict_transaction.html'
	elif report_name == 'G2CServices':
		templ_name = TEMPL_DIR + '/g2c_service.html'

	return templ_name

def _getFilteredResult(queryset,district,yyyymm):

	filtered_result = [ q for i,q in enumerate(queryset) if q.district==district and re.match(yyyymm,q.updated_date) ]

	return filtered_result
def _getTodayDate():
	timestamp  = timezone.now()
	return timestamp.strftime('%Y%m%d')
def _isReportInProgress(district,user,report_type):
	state = None
	try:
		snapshot=ReportSnapShot.objects.filter( Q(district=district), Q(state='submitted')|Q(state='inprogress'), Q(owner=user), Q(report_type=report_type) )
		if snapshot:
			state = True
		else:
			state = False
	except ReportSnapShot.DoesNotExist:	
		state = False

	return state
def _convertStringToByte(s):
	lst = []
	for ch in s:
		hv = hex(ord(ch)).replace('0x', '')
		if len(hv) == 1:
			hv = '0'+hv
		lst.append(hv)
	hex_str =''.join( lst )
	bytes = []

	hexStr = ''.join( hex_str.split(" ") )

	for i in range(0, len(hexStr), 2):
		bytes.append( chr( int (hexStr[i:i+2], 16 ) ) )

	return ''.join( bytes )