
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django_tables2 import RequestConfig
from django.db import IntegrityError


from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.utils import timezone
from django.middleware.csrf import get_token

from .models import ReportSnapShot,Comment
from .forms import CommentForm,ReportForm
from .tables import SimpleTable
from reports.models import *
from .utils import render_to_pdf
import binascii
import re
from django.db import connection, transaction
from django.http import Http404
from mysite.custom_config import *
# Create your views here.
dict_q = {}
report_templates = { 'Manpower' : 'reviewer/mp.html',
					 'CSC' : 'reviewer/csc.html',
					 'Software' : 'reviewer/software.html',
					 'Hardware' : 'reviewer/hardware.html',
					 'NOFN' : 'reviewer/nofn.html',
					 'SWAN' : 'reviewer/swan.html',
					 'DigitalLiteracy' : 'reviewer/digital_literacy.html',
					 'eDistrictTrans' : 'reviewer/edistrict_transactioin.html',
					 'G2CServices' : 'reviewer/g2c_service.html'
					}
pdf_templates = {
					'Manpower' : 'reviewer/manpower_pdf.html',
					'CSC' : 'reviewer/csc_pdf.html',
					 'Software' : 'reviewer/software_pdf.html',
					 'Hardware' : 'reviewer/hardware_pdf.html',
					 'NOFN' : 'reviewer/nofn_pdf.html',
					 'SWAN' : 'reviewer/swan_pdf.html',
					 'DigitalLiteracy' : 'reviewer/digital_literacy_pdf.html',
					 'eDistrictTrans' : 'reviewer/edistrict_transactioin_pdf.html',
					 'G2CServices' : 'reviewer/g2c_service_pdf.html'
	
}
snapshots = {}
@login_required
def generateReport(request):
	
	if request.method == 'POST':
		form = ReportForm(request.POST)
		null_string = 'No results to display'
		district_dict = dict(DISTRICT_CHOICES)
		if form.is_valid():
			
			district = form.cleaned_data['district']
			district_full_name = district_dict[district]
			report_name = form.cleaned_data['report_name']
			YYYYMM = form.cleaned_data['YYYYMM']
			queryset = ReportSnapShot.objects.filter(district=district,YYYYMM=YYYYMM,state='submitted',report_type=report_name)
			if queryset.exists():
				print "Populating Snapshot from database"
				filtered_result = _massage_content(str(queryset))
				if len(filtered_result) == 0:
					return render(request,'reviewer/empty_results.html',{'null_string':null_string,'report_name':report_name,'district':district_full_name,'YYYYMM':YYYYMM} )
				else:
					dict_q[report_name.encode('ascii')] = filtered_result
					print "updating state of snapshot"
					#queryset.update(state='inprogress')
					return render(request,'reviewer/snapshot.html',{'user':request.user,'filtered_result':filtered_result})
					#return HttpResponse(filtered_result)
			else:
				queryset = _getSpecficModelQuerySet(report_name)

				filtered_result = _getFilteredResult(queryset,district,YYYYMM)

				dict_q[report_name.encode('ascii')] = filtered_result
				if len(filtered_result) == 0:
					return render(request,'reviewer/empty_results.html',{'null_string':null_string,'report_name':report_name,'district':district_full_name,'YYYYMM':YYYYMM} )

				else:	
									
					timestamp  = timezone.now()
					today_date=timestamp.strftime('%Y%m%d')
					#print(filtered_result)
					context = {'filtered_result':filtered_result,'report_name':report_name,'district_full_name':district_full_name,'YYYYMM':YYYYMM,'today_date':today_date,'district':district,'csrf':1,'include_href':1}
					templ_name = report_templates[report_name]
		
				

					return render(request,templ_name,context )


		else:
			print form.errors
	else:
		form=ReportForm() 

	return render(request,'reviewer/generate_report.html',{'form':form})      

def generatePDF(request):
	district = request.GET.get('district')
	report_month = request.GET.get('period')
	report_name = request.GET.get('report').encode('ascii')
	#filtered_result = request.GET.get('report_data')
	#filtered_result = dict_q[report_name]
	queryset = _getSpecficModelQuerySet(report_name)

	filtered_result = _getFilteredResult(queryset,district,report_month)
	pdf_templ = pdf_templates[report_name]
	data = { 'report_month':report_month,'report_name': report_name,'district':district, 'filtered_result':filtered_result }
	pdf = render_to_pdf(pdf_templ, data)
	
	#return HttpResponse(dis)

	return HttpResponse(pdf, content_type='application/pdf')


def handleComments(request):

	report_name = ''
	today = ''
	context = {}
	
	if request.method == 'POST':
		form = CommentForm(request.POST)
		report_name = request.POST.get("report_name", "")
		today = request.POST.get("today", "")
		YYYYMM = today[0:6]
		district = request.POST.get("district", "")
		#content_id = request.POST.get("content_id", "")
		post = get_object_or_404(ReportSnapShot,report_type=report_name,district=district,YYYYMM=YYYYMM)
		if form.is_valid():
			 new_comment = form.save(commit=False)
			 new_comment.post = post
			 new_comment.user = request.user
			 new_comment.status = 'raised'
			 new_comment.comment_to = post.owner
			 new_comment.save()
			 return HttpResponse("Comment Recorded Successfully")
		else:
			print form.errors
	else:

		post_id = request.GET.get('id')
		if post_id:
			post_id = int(post_id)
		if not post_id:
			report_name = request.GET.get('report').encode('ascii')
			today = request.GET.get('today').encode('ascii')
			YYYYMM = today[0:6]
			district = request.GET.get('district').encode('ascii')
			#content_id =request.GET.get('content_id').encode('ascii')
			post = get_object_or_404(ReportSnapShot,report_type=report_name,district=district,YYYYMM=YYYYMM)
			obj = Comment.objects.filter(post_id=post.id,status='raised')

			if obj.exists():
				return HttpResponse("A comment has been already been raised by you on this report which is not yet answered")
			else:
				
				form=CommentForm() 
				context = {'form':form,'user':request.user,'report_name':report_name, 'today':today,'district': district,'new_comment':1}
		else:
			data = Comment.objects.filter(post_id=post_id,status='raised').values('body','user')
			body = data[0]['body'] + "<< " + data[0]['user']
			form=CommentForm({'name': request.user.username,'body':body}) 
			context = {'form':form,'user':request.user,'response_to_comment':1}


	return render(request,'reviewer/comment.html',context)       

def populateComment(request):
	status = request.GET.get('status').encode('ascii')
	logged_in_user = request.GET.get('user').encode('ascii')
	user_group = request.GET.get('group').encode('ascii')
	if user_group == 'Applicant':
		result_set = Comment.objects.filter(status='raised',comment_to=logged_in_user,active=True)
	elif user_group == 'Reviewer':	
		result_set = Comment.objects.filter(user=logged_in_user).exclude(status='closed')
	filtered_result = []
	
	#filtered_result = [ q for i,q in enumerate(result_set) if q.active and q.status == status ]
	filtered_result = result_set
	required_list = {}
	count = 1
	for i in filtered_result:
		snapshot_id = i.post_id
		print(snapshot_id)
		snapshot =str( ReportSnapShot.objects.filter(id=snapshot_id) )
		s = snapshot.replace("[<ReportSnapShot:","")
		s = s.replace("</html> >]","</html>")
		snapshots[str(snapshot_id)] = s
		count = count + 1
	#print required_list
	templ = 'reviewer/show_comments.html'

	return render(request,templ,{'filtered_result': filtered_result})

def populateSnapshot(request):
	id = str ( request.GET.get('id').encode('ascii') )
	#print(id)
	return HttpResponse(snapshots[id])

"""""
Private Routines
"""
def _massage_snapshot(content):
	
	s1 = snapshot.replace("[<ReportSnapShot:","")
	#s = s1.replace("</html> >]","</html>")
	s = re.sub(r"^>\]","",s1)
	print(s)




def _getSpecficModelQuerySet(report_name):
	if report_name == 'Manpower':
		return  ManpowerReport.objects.all()
	elif report_name == 'CSC':
		return  CSCReport.objects.all()
	elif report_name == 'SWAN':
		return SWANReport.objects.all()
	elif report_name == 'NOFN':
		return SWANReport.objects.all()
	elif report_name == 'Hardware':
		return HardwareReport.objects.all()
	elif report_name == 'Software':
		return SoftwareReport.objects.all()
	elif report_name == 'DigitalLiteracy':
		return DLReport.objects.all()
	elif report_name == 'eDistrictTrans':
		return ServiceTransReport.objects.all()
	elif report_name == 'G2CServices':
		return g2cServiceReport.objects.all()

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


def _convertByteToStr(byteStr):
	print('F:')
	print (byteStr)
	hex_str = ' '.join( [ "%02X" % ord( x ) for x in byteStr ] )
	
	return  hex_str and chr(atoi(hex_str[:2], base=16)) + toStr(hex_str[2:]) or ''




def _getFilteredResult(queryset,district,yyyymm):

	filtered_result = [ q for i,q in enumerate(queryset) if q.district==district and re.match(yyyymm,q.updated_date) ]

	return filtered_result

def _massage_content(snapshot):
	
	s1 = snapshot.replace("[<ReportSnapShot:","")
	#s = s1.replace("</html> >]","</html>")
	s = re.sub(r"^>\]","",s1)
	print(s)

	return s
# def _rawSQLQuery(report_name):
# 	cursor = connection.cursor();
# 	query = "select s.id from reviewer_reportsnapshot s, reviewer_comment c where c.post_id=s.id and c.active=1 and s.report_name=report_name"