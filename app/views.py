from django.shortcuts import render
from django.http import *
from . import *
from django.shortcuts import redirect
from django.urls import reverse
from django.template import loader
from app.models import JobPost

# Create your views here.

# jobinformation = {
#     'title1':"First job",
#     'discription1':"This is a First job discription ",
#     'title2':"second job",
#     'discription2':"This is second job description"
# }
jobTitle = [
    "First Title",
    "Second Title",
    "Third Title"
]
jobDetail = [
    "First job Discription",
    "Second JOb Discription",
    "Third JOb Discription"
]

# def hello(request):
#     return HttpResponse('<h1 style="text-align:center;">Hello World</h1>')

class tempClass():
    x=5

def indexx(request):
    # template = loader.get_template('app/index.html')
    list = ["ALPHA","BETA","GAMMA"]
    temp_obj= tempClass()
    is_authenthicated = False
    context={"name":"Django","age":21,"first_list":list,"temp_object":temp_obj,
            "is_authenthicated":is_authenthicated}
    # return HttpResponse(template.render(context,request))
    return render(request,'app/index.html',context)


def job_list(request):
    # list_of_jobs = "<ul>"
    # for j in jobTitle:
    #     job_id = jobTitle.index(j) 
    #     detail_url =  reverse('jobs_detail',args=(job_id,))
    #     list_of_jobs += f"<li><a href='{detail_url}'>{j}</a></li>"
    # list_of_jobs += "</ul>"
    # return HttpResponse(list_of_jobs)
    jobs = JobPost.objects.all()
    context = {"jobs":jobs}
    return render(request,'app/jobs.html',context)

def jobDetail1(request,id):
    # return HttpResponse(f'<h1 style="text-align:center";>Job Detail Page {id}</h1>')
    # site = "https://www.google.com"
    # return HttpResponse(f"<h2 style='text-align:center;font-size:2rem;'>This is a Link to <a href='{site}' style='text-decoration:none; text-align:center; font-family:\"Roboto\",sans-serif;font-size:2.5rem;'>  Google.com </a> for a job id {id}</h2>")
     
    try:
        # context={'job_detail':jobDetail[id],'job_title':jobTitle[id]}

        if id==0:
            return redirect(reverse('jobs_home'))
        # return_html = f"<h1>{jobTitle[id]}</h1> <h2>{jobDetail[id]}</h2>"
        # return HttpResponse(f"This job is {return_html}")
        job = JobPost.objects.get(id = id)
        context={'job':job}
        return render(request,'app/jobdetail.html',context)
    except:
        return HttpResponseNotFound("<h1 style=\"font-family:'Roboto',sans-serif;font-size:2rem;text-align:center;font-weight:700;align-items:center;color:#4b4b4b;\">PAGE NOT FOUND</h1>")

def job_number(request,id):
    try:
        if id == 0:
            return redirect(reverse('job_home'))
        return HttpResponse(reverse('job_home'))
    except:
        return HttpResponseNotFound("<h1 style=\"font-family:'Roboto',sans-serif;font-size:2rem;text-align:center;font-weight:700;align-items:center;color:#4b4b4b;\">PAGE NOT FOUND</h1>")