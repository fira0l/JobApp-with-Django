from django.shortcuts import render

from uploadapp.forms import UploadForm
from uploadapp.forms import UploadFileForm

# Create your views here.

def uploadImage(request):
    if request.method=='POST':
        form = UploadForm(request.POST,request.FILES)
        if form.is_valid:
            form.save()
            saved_object = form.instance
            return render(request,'uploadapp/addImage.html',{'form':form,'saved_object':saved_object})
    else:
        form = UploadForm()
    return render(request,'uploadapp/addImage.html',{'form':form})

def upload_file(request):
    if request.method=='POST':
        form = UploadFileForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            saved_object = form.instance
            return render(request,'uploadapp/addfile.html',{'form':form,'saved_object':saved_object})
    else:
        form = UploadFileForm()
    return render(request,'uploadapp/addfile.html',{'form':form})
