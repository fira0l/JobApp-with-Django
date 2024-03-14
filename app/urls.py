from django.urls import path
from jobapp import urls
from app.views import * 
# from app.views import hello,jobDetail1

urlpatterns = [
 path('',job_list,name='jobs_home'),
 path('hello/',indexx,name='indexx'),
 path('job/<int:id>',jobDetail1,name='jobs_detail'),
 path('<int:id>',job_number),
]