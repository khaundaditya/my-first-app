from django import forms

from .models import HardwareReport,ManpowerReport,CSCReport,SWANReport,DigitalLiteracyReport,NOFNReport,SoftwareReport,DISTRICT_CHOICES


class ManpowerReportForm(forms.ModelForm):

	class Meta:
		model = ManpowerReport
		exclude = ('updated_date','user_name')

class HardwareReportForm(forms.ModelForm):


	class Meta:
		model = HardwareReport
		exclude = ('updated_date',)
class CSCReportForm(forms.ModelForm):
	class Meta:
		model = CSCReport
		exclude = ('updated_date','user_name',)

class SWANReportForm(forms.ModelForm):
	class Meta:
		model = SWANReport
		exclude = ('updated_date','user_name',)

class DigitalLiteracyReportForm(forms.ModelForm):
	class Meta:
		model = DigitalLiteracyReport
		exclude = ('updated_date',)


class NOFNReportForm(forms.ModelForm):
	class Meta:
		model = NOFNReport
		exclude = ('updated_date',)

class SoftwareReportForm(forms.ModelForm):
	class Meta:
		model = SoftwareReport
		exclude = ('updated_date',)


class UpdateSnapshot(forms.Form):
	Reports = (
		 ('-------', ("--------")),
       ('Manpower', ("Manpower Report")),
       ('CSC', ("CSC Report")), 
       ('Hardware', ("Hardware Report")),
       ('Software', ("Software Report")),
       ('SWAN', ("SWAN Report")),
       ('NOFN', ("NOFN Report")),
       ('DigitalLiteracy', ("Digital Literacy Report")),

   )
	district = forms.ChoiceField(choices=DISTRICT_CHOICES,label="District")
	report_name = forms.ChoiceField(choices=Reports,label="Report Name")
	YYYYMM= forms.CharField(required=True,label="YYYYMM")
