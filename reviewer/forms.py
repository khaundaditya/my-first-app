from django import forms
from .models import Comment
#from .models import DISTRICT_CHOICES
from mysite.custom_config import *
class ReportForm(forms.Form):
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
	report_name = forms.ChoiceField(choices=REPORT_NAMES,label="Report Name")
	YYYYMM= forms.CharField(required=True,label="YYYYMM")

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')
  