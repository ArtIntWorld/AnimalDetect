from django.shortcuts import render
from django.http import HttpResponse
from .models import*

# Create your views here.
def login(request):
    return render(request,"public/login.html")

def signup(request):
    return render(request,'public/signup.html')

def forestdivision(request):
    return render(request,'admin/forestdivision.html')

def foreststation(request):
    return render(request,'admin/foreststation.html')

def animal(request):
    return render(request,'admin/animal.html')

def reply(request):
    return render(request,'admin/reply.html')

def complaintcheck(request):
    return render(request,'forest_station/complaintcheck.html')

def alertnotify(request):
    return render(request,'forest_station/alertnotify')

def complaintreq(request):
    return render(request,'user/complaintrequest.html')

def complaintverified(request):
    return render(request,'user/complaintverified.html')

def notification(request):
    return render(request,'user/notification.html')