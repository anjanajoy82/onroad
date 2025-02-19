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
    

def view_near_pump(request):
    pumps=Register.objects.filter(usertype="petrol", is_approved=True)
    return render(request,'view_near_mech.html',{'mechanics':pumps})

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

def view_booking(request):
    user=request.user
    bookings=MechBooking.objects.filter(mechanic=user)
    return render(request,'bookings.html',{'bookings':bookings})


def approve_booking(request,id):
    booking=MechBooking.objects.get(id=id)
    booking.status = "Approved"
    subject="Booking Approval Notification"
    message=f"Dear {booking.user.username} Your booking is being approved. Please wait while we reach there with neccessary tools...."
    email_from=[booking.mechanic.email]
    email_to=[booking.user.email]
    send_mail(subject, message, email_from, email_to)
    messages.success(request,'Booking Approved and send mail successfully.',extra_tags="success")
    return redirect('bookings')


def reject_booking(request,id):
    booking=MechBooking.objects.get(id=id)
    booking.status = "Rejected"
    subject="Booking Rejection Notification"
    message=f"Dear {booking.user.username} Your booking is being rejected because of other emergencies.. Please contact other mechanics....."
    email_from=[booking.mechanic.email]
    email_to=[booking.user.email]
    send_mail(subject, message, email_from, email_to)
    messages.success(request,'Booking rejected and send mail successfully.',extra_tags="success")
    return redirect('bookings')


def update_status(request,id):
    booking=MechBooking.objects.get(id=id)
    if booking.status == "Approved":
        booking.status = "On the way"
        booking.save()
    elif booking.status == "On the way":
        booking.status = "Working"
        booking.save()
    elif booking.status == "Working":
        booking.status = "Completed"
        booking.save()
    else:
        booking.status="Not completed"
        booking.save()
    return redirect('bookings')
    