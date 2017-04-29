from django.conf.urls import url
from . import views


urlpatterns = [
	
	url(r'^generate_report/$',views.generateReport,name='generate_report'),
	url(r'^generate_PDF/$',views.generatePDF,name='generate_pdf'),
	url(r'^reviewer_comment/$',views.handleComments,name='reviewer_comment'),
	url(r'^populate_comment/$',views.populateComment,name='populate_comment'),
	url(r'^populate_snapshot/$',views.populateSnapshot,name='populate_snapshot'),
]