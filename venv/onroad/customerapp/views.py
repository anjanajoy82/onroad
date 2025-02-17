from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from .models import *
from .forms import *
from django.conf import settings
from django.core.mail import send_mail
import secrets,string
from onroadapp.models import *


# Create your views here.

def view_near_mech(request):
    mechanics=Register.objects.filter(usertype="mechanic", is_approved=True)
    return render(request,'view_near_mech.html',{'mechanics':mechanics})

def mechanic_profile(request):
    mechanic=request.user
    mechanic=Register.objects.get(id=mechanic.id)
    return render(request,'mechanic_profile.html',{'mechanic':mechanic})
    

def view_near_pump(request):
    pumps=Register.objects.filter(usertype="petrol", is_approved=True)
    return render(request,'view_near_mech.html',{'mechanics':pumps})