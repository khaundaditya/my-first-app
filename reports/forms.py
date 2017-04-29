from django import forms
from mysite.custom_config import *
from .models import *


class ManpowerReportForm(forms.ModelForm):

	class Meta:
		model = ManpowerReport
		exclude = ('updated_date','user_name')

class HardwareReportForm(forms.ModelForm):

	class Meta:
		model = HardwareReport
		exclude = ('updated_date','user_name')
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
		model = DLReport
		exclude = ('updated_date','user_name',)


class NOFNReportForm(forms.ModelForm):
	class Meta:
		model = NOFNReport
		exclude = ('updated_date','user_name')

class SoftwareReportForm(forms.ModelForm):
	class Meta:
		model = SoftwareReport
		exclude = ('updated_date','user_name')
class G2CServiceReportForm(forms.ModelForm):
	class Meta:
		model = g2cServiceReport
		exclude = ('updated_date','associated_line_department','user_name')
class eDistrictReportForm(forms.ModelForm):
	class Meta:
		model = ServiceTransReport
		exclude = ('updated_date','associated_line_department','user_name')
class UpdateSnapshot(forms.Form):

	district = forms.ChoiceField(choices=DISTRICT_CHOICES,label="District")
	report_name = forms.ChoiceField(choices=REPORT_NAMES,label="Report Name")
	YYYYMM= forms.CharField(required=True,label="YYYYMM")
 