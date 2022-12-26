from django.shortcuts import render
from .forms import ModelFileUploadForm
from django.http import HttpResponse
# Create your views here.
from .models import ProjectFiles
def home(request):
	files = ProjectFiles.objects.all()

	if request.method == 'POST':
		form = ModelFileUploadForm(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			return HttpResponse("Uploaded Success fully <a href='/'}>Home</a>")
	else:
		form = ModelFileUploadForm()
	context = {'form':form,'files':files}
	return render(request,'index.html',context)