from django.shortcuts import render
from subscribe.models import Subscribe
from subscribe.forms import SubscribeForm
from django.shortcuts import redirect
from django.urls import reverse
# Create your views here.

def thank_you(request):
    context={}
    return render(request,'subscribe/thank_you.html',context)

def subscribe(request):
    subscribe_form= SubscribeForm()
    error_empty_email = ''
    if request.POST:
        subscribe_form = SubscribeForm(request.POST)
        if subscribe_form.is_valid():
            subscribe_form.save()
            # print("valid Form") 
            # print(subscribe_form.cleaned_data)
            # email = subscribe_form.cleaned_data['email']
            # first_name = subscribe_form.cleaned_data['first_name']
            # last_name = subscribe_form.cleaned_data['last_name']
            # subscribe = Subscribe(first_name = first_name,last_name=last_name,email=email)
            # subscribe.save()
            return redirect(reverse('thank_you'))
    context={
        "form":subscribe_form,
        "error_empty_email":error_empty_email,
        }
    return render(request,'subscribe/subscribe.html',context)
