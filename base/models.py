from django.db import models

# Create your models here.
class ProjectFiles(models.Model):
	title = models.CharField(max_length=200)
	file = models.FileField(upload_to='uploads/',null=True)
	image =models.ImageField(upload_to='images/',null=True)

	def __str__(self):
		return self.title