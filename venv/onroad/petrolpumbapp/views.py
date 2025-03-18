from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from customerapp.models import *
from .forms import *
from .models import *
from django.conf import settings
from django.core.mail import send_mail
import secrets,string
from onroadapp.models import *

# Create your views here.
def view_pumbbooking(request):
    user = request.user.id
    bookings = PetrolBooking.objects.filter(petrol=user)  # Correct filter condition
    print(bookings)
    return render(request, 'bookings_pumb.html', {'bookings': bookings})


def pumb_approve_booking(request,id):
    booking=PetrolBooking.objects.get(id=id)
    booking.status = "Approved"
    booking.save()
    subject="Booking Approval Notification"
    message=f"Dear {booking.user.username} Your booking is being approved. Please wait while we reach there...."
    email_from=settings.EMAIL_HOST_USER
    email_to=[booking.user.email]
    send_mail(subject, message, email_from, email_to,fail_silently=True)
    messages.success(request,'Booking Approved and send mail successfully.',extra_tags="success")
    return redirect('bookings_pumb')


def pumb_reject_booking(request,id):
    booking=PetrolBooking.objects.get(id=id)
    booking.status = "Rejected"
    booking.save()
    subject="Booking Rejection Notification"
    message=f"Dear {booking.user.username} Your booking is being rejected because of fuel insufficiency.. Please contact other petrol pumps....."
    email_from=settings.EMAIL_HOST_USER
    email_to=[booking.user.email]
    send_mail(subject, message, email_from, email_to,fail_silently=True)
    messages.success(request,'Booking rejected and send mail successfully.',extra_tags="success")
    return redirect('bookings_pumb')


def pumb_update_status(request,id):
    booking=PetrolBooking.objects.get(id=id)
    if booking.status == "Assigned":
        subject="Booking Status Notification"
        message=f"Dear {booking.user.username}, A delivery agent have been assigned to you. He will update you about the delivery."
        email_from=settings.EMAIL_HOST_USER
        email_to=[booking.user.email]
        send_mail(subject, message, email_from, email_to, fail_silently=True)
        booking.status = "On the way"
        booking.save()
       
    elif booking.status == "On the way":
        booking.status = "Reached"
        booking.save()
    elif booking.status == "Reached":
        subject="Booking Status Notification"
        message=f"Dear {booking.user.username} Your delivery is reached. Thank you for contacting us. Please contact for any further assistance. "
        email_from=settings.EMAIL_HOST_USER
        email_to=[booking.user.email]
        send_mail(subject, message, email_from, email_to, fail_silently=True)
        booking.status = "Delivered"
        booking.save()
        
    else:
        booking.status="Assigned"
        booking.save()
    return redirect('delivery_agent_bookings')
    

def assign_delivery_agent(request, booking_id):
    booking = get_object_or_404(PetrolBooking, id=booking_id)

    # Fetch delivery agents under the current petrol pump
    delivery_agents = Register.objects.filter(usertype='deliveryagent', pump_id=request.user.id)
    print(delivery_agents)

    if request.method == "POST":
        agent_id = request.POST.get('delivery_agent')
        selected_agent = get_object_or_404(Register, id=agent_id)

        # Assign the selected delivery agent
        booking.delivery_agent = selected_agent
        booking.status = "Assigned"
        booking.save()

        return redirect('bookings_pumb')

    return render(request, 'assign_delivery_agent.html', {'booking': booking, 'delivery_agents': delivery_agents})


def delivery_agent_bookings(request):
    # Fetch bookings assigned to the logged-in delivery agent
    bookings = PetrolBooking.objects.filter(delivery_agent=request.user)

    return render(request, 'delivery_booking.html', {'bookings': bookings})

def petrol_pump_dashboard(request):
    return render(request, 'petrol_pump_dashboard.html')


def add_fuel_detail(request):
    if request.method == "POST":
        form = FuelForm(request.POST,request.FILES)
        if form.is_valid():
            fuel_detail = form.save(commit=False)
            fuel_detail.petrol_pump = request.user  # Assign current petrol pump user
            fuel_detail.save()
            return redirect('view_fuel_details')  # Redirect after adding fuel
    else:
        form = FuelForm()
    return render(request, 'add_fuel_detail.html', {'form': form})


def view_fuel_details(request):
    fuel_detail = FuelDetails.objects.filter(petrol_pump=request.user)
    return render(request, 'view_fuel_detail.html', {'fuel_detail': fuel_detail})


def delete_fuel(request,id):
    fuel=FuelDetails.objects.get(id=id)
    fuel.delete()
    return redirect('view_fuel_details')




def view_petrol_feedbacks(request):
    id=request.user.id 
    feedbacks = PetrolFeedback.objects.filter(petrol=id).order_by('-created_at')  # Retrieve all feedbacks
    return render(request, 'view_feedbacks.html', {'feedbacks': feedbacks})



