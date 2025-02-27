from django.db import models

from onroadapp.models import *

# Create your models here.
class MechBooking(models.Model):
    user=models.ForeignKey(Register, on_delete=models.CASCADE,null=True,related_name='user')
    mechanic=models.ForeignKey(Register, on_delete=models.CASCADE,null=True,related_name='mechanic')
    name=models.CharField(max_length=50,null=True)
    description=models.CharField(max_length=500,null=True)
    current_loc=models.URLField(max_length=255, null=True)
    vehicle_type=models.CharField(max_length=50,null=True)
    status=models.CharField(max_length=10,default="Pending")
    booked_at = models.DateTimeField(auto_now_add=True, null=True)
    f_status = models.BooleanField(default=False)




class PetrolBooking(models.Model):
    # Linking to the same user and mechanic models
    user = models.ForeignKey(Register, on_delete=models.CASCADE, null=True, related_name='customer')
    petrol = models.ForeignKey(Register, on_delete=models.CASCADE, null=True, related_name='petrol')
    # Fields for fuel request 
    name = models.CharField(max_length=50, null=True)
    description = models.CharField(max_length=500, null=True)
    current_loc = models.URLField(max_length=255, null=True)
    vehicle_type = models.CharField(max_length=50,null=True)
    # Additional fields specific to petrol booking
    fuel_type = models.CharField(max_length=50, null=True)
    fuel_quantity = models.DecimalField(max_digits=5, decimal_places=2, null=True)  # Liters or Gallons
    booked_at = models.DateTimeField(auto_now_add=True,null=True)  # Preferred time for delivery
    urgency = models.CharField(max_length=10,default='not urgent')
     # Address details
    delivery_address = models.CharField(max_length=255, null=True)
    # Payment Method
    payment_method = models.CharField(max_length=20,default='cash_on_delivery')
    # Status of the request (Pending, Approved, Completed, Rejected)
    status = models.CharField(max_length=10, default="Pending")

    delivery_agent = models.ForeignKey(Register, on_delete=models.SET_NULL, null=True, blank=True, related_name='assigned_deliveries')

    def __str__(self):
        return f"Petrol Booking for {self.name} - {self.fuel_type} ({self.status})"



class MechFeedback(models.Model):
    booking = models.ForeignKey(MechBooking, on_delete=models.CASCADE,related_name="booking")  # Linking feedback to a user
    user = models.ForeignKey(Register, on_delete=models.CASCADE,related_name="user_feed")  # Linking feedback to a user
    mechanic = models.ForeignKey(Register,on_delete=models.CASCADE,null=True,related_name="mech_feedback")
    message = models.TextField(max_length=500,null=True)  # Feedback content
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)], default=5)  # Rating from 1 to 5
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for when feedback was created

    def __str__(self):
        return f"Feedback from {self.user.username} - {self.rating} stars"



class PetrolFeedback(models.Model):
    booking = models.ForeignKey(PetrolBooking, on_delete=models.CASCADE,related_name="booking")  # Linking feedback to a user
    user = models.ForeignKey(Register, on_delete=models.CASCADE,related_name="user_feedback")  # Linking feedback to a user
    petrol = models.ForeignKey(Register,on_delete=models.CASCADE,null=True,related_name="petrol_feedback")
    message = models.TextField(max_length=500,null=True)  # Feedback content
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)], default=5)  # Rating from 1 to 5
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for when feedback was created

    def __str__(self):
        return f"Feedback from {self.user.username} - {self.rating} stars"
