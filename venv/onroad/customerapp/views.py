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

def view_details(request,id):
    mechanic=Register.objects.get(id=id)
    return render(request,'view_details.html',{'mechanic':mechanic})
    
def view_pumbdetails(request,id):
    petrol=Register.objects.get(id=id)
    return render(request,'view_pumbdetails.html',{'petrol':petrol})

def view_near_pump(request):
    pumps=Register.objects.filter(usertype="petrol", is_approved=True)
    return render(request,'view_near_pumb.html',{'mechanics':pumps})

def booking(request,id):
    mech = Register.objects.get(id=id)
    if request.method == 'POST':
        form = MechForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.user=request.user
            book.mechanic= mech
            book.status = "Booked"
            book.save()
            messages.success(request, "Booking successfull.", extra_tags="success")
            return redirect('view_near_mech')  # Redirect to the profile page
        else:
            messages.error(request, "Profile update failed. Please check your form.", extra_tags="error")
    else:
        form = MechForm()

    return render(request, 'mechbooking.html', {'form': form})



def pumb_booking(request,id):
    pumb = Register.objects.get(id=id)
    if request.method == 'POST':
        form = PetrolForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.user=request.user
            book.petrol= pumb
            book.status = "Booked"
            book.save()
            messages.success(request, "Booking successfull.", extra_tags="success")
            return redirect('view_near_pump')  # Redirect to the profile page
        else:
            messages.error(request, "Profile update failed. Please check your form.", extra_tags="error")
    else:
        form = PetrolForm()

    return render(request, 'pumbbooking.html', {'form': form})


def view_mech_bookings(request):
    user=request.user
    bookings=MechBooking.objects.filter(user=user)
    return render(request,'view_mech_bookings.html',{'bookings':bookings})

def view_pumb_bookings(request):
    user=request.user
    bookings=PetrolBooking.objects.filter(user=user)
    return render(request,'view_pumb_bookings.html',{'bookings':bookings})

