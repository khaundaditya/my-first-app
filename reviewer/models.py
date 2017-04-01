from django.db import models
import base64
import uuid
# Create your models here.
# class Base64Field(models.TextField):

#     def contribute_to_class(self, cls, name):
#         if self.db_column is None:
#             self.db_column = name
#         self.field_name = name + '_base64'
#         super(Base64Field, self).contribute_to_class(cls, self.field_name)
#         setattr(cls, name, property(self.get_data, self.set_data))

#     def get_data(self, obj):
#         return base64.decodestring(getattr(obj, self.field_name))

#     def set_data(self, obj, data):
#         setattr(obj, self.field_name, base64.encodestring(data))


class ReportSnapShot(models.Model):
	content_uuid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
	content = models.BinaryField(default='')
	owner = models.CharField(max_length=20)
	YYYYMM = models.CharField(max_length=6,default='')
	district = models.CharField(max_length=2,default='')
	#created = models.DateTimeField(auto_now_add=True)
	#updated = models.DateTimeField(auto_now=True)
	report_type = models.CharField(max_length=20,default='abc')
	state = models.CharField(default='',max_length=20)
	#report_submitted_by = models.CharField(default='',max_length=20)
	def __str__(self):
		return "{0}".format( self.content)
	class Meta:
		unique_together=(( 'district','owner'),)

class Comment(models.Model):
	#post =  models.UUIDField(unique=True,default=uuid.uuid4, editable=False)
	post = models.ForeignKey(ReportSnapShot,related_name='comments',default='')
	name = models.CharField(max_length=80)
	user = models.CharField(max_length=20,default='')
	email = models.EmailField()
	body = models.TextField()
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	active = models.BooleanField(default=True)
	status = models.CharField(max_length=12, default='raised')
	comment_to = models.CharField(max_length=20,default='')
	class Meta:
	    ordering = ('created',)

	def __str__(self):
	   # return 'Comment by {} on {}'.format(self.name, self.post,)
	    return "{0} {1} {2} {3} {4} {5} {6}".format( self.body,self.active,self.status,self.updated,self.post_id,self.comment_to,self.user)