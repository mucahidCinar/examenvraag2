from django.db import models

# Create your models here.
class Examen(models.Model):
	student_name = models.CharField(max_length=50)
	exaam_name = models.CharField(max_length=50)
	date = models.DateField(max_length=50)
	reden = models.CharField(max_length=500)
	
	def __unicode__(self):
		return self.student_name

