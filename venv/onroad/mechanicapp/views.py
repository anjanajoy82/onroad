from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from customerapp.models import *
from .forms import *
from django.conf import settings
from django.core.mail import send_mail
import secrets,string
from onroadapp.models import *


# Create your views here.
def view_booking(request):
    user=request.user
    bookings=MechBooking.objects.filter(mechanic=user)
    return render(request,'bookings.html',{'bookings':bookings})


def approve_booking(request,id):
    booking=MechBooking.objects.get(id=id)
    booking.status = "Approved"
    booking.save()
    subject="Booking Approval Notification"
    message=f"Dear {booking.user.username} Your booking is being approved. Please wait while we reach there with neccessary tools...."
    email_from=settings.EMAIL_HOST_USER
    email_to=[booking.user.email]
    send_mail(subject, message, email_from, email_to,fail_silently=True)
    messages.success(request,'Booking Approved and send mail successfully.',extra_tags="success")
    return redirect('bookings')


def reject_booking(request,id):
    booking=MechBooking.objects.get(id=id)
    booking.status = "Rejected"
    booking.save()
    subject="Booking Rejection Notification"
    message=f"Dear {booking.user.username} Your booking is being rejected because of other emergencies.. Please contact other mechanics....."
    email_from=settings.EMAIL_HOST_USER
    email_to=[booking.user.email]
    send_mail(subject, message, email_from, email_to, fail_silently=True)
    messages.success(request,'Booking rejected and send mail successfully.',extra_tags="success")
    return redirect('bookings')


def mech_update_status(request,id):
    booking=MechBooking.objects.get(id=id)
    if booking.status == "Approved":
        subject="Booking Status Notification"
        message=f"Dear {booking.user.username}, Your assistance is on the way. Please wait patiently. Will reach in short. Please feel free to ontact us anytime for any help."
        email_from=settings.EMAIL_HOST_USER
        email_to=[booking.user.email]
        send_mail(subject, message, email_from, email_to, fail_silently=True)
        booking.status = "On the way"
        booking.save()
    elif booking.status == "On the way":
        booking.status = "Working"
        booking.save()
    elif booking.status == "Working":
        subject="Booking Status Notification"
        message=f"Dear {booking.user.username} Your work is completed. Thank you for contacting us. Please contact for any further assistance. "
        email_from=settings.EMAIL_HOST_USER
        email_to=[booking.user.email]
        send_mail(subject, message, email_from, email_to, fail_silently=True)
        booking.status = "Completed"
        booking.save()
    else:
        booking.status="Approved"
        booking.save()
    return redirect('bookings')
    
def view_mech_feedbacks(request):
    id=request.user.id
    feedbacks = MechFeedback.objects.filter(mechanic=id).order_by('-created_at')  # Retrieve all feedbacks
    return render(request, 'view_feedbacks.html', {'feedbacks': feedbacks})
