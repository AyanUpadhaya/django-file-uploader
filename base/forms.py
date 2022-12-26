from django import forms
from django.forms import ModelForm
from .models import ProjectFiles

class ModelFileUploadForm(ModelForm):
	class Meta:
		model = ProjectFiles
		# fields = '__all__'
		fields = ['title','file']

		widgets={
            'title':forms.TextInput(attrs={'class':"form-control",'placeholder':'Enter File Name'}),
            'file':forms.FileInput(attrs={'class':"form-control mt-4"}),
 

        }
