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
    urgency_choices = [
        ('immediate', 'Immediate'),
        ('can_wait', 'Can Wait'),
    ]
    urgency = models.CharField(max_length=10, choices=urgency_choices, default='can_wait')
     # Address details
    delivery_address = models.CharField(max_length=255, null=True)
    # Payment Method
    payment_method_choices = [
        ('cash_on_delivery', 'Cash on Delivery'),
    ]
    payment_method = models.CharField(max_length=20, choices=payment_method_choices, default='cash_on_delivery')
    # Status of the request (Pending, Approved, Completed, Rejected)
    status = models.CharField(max_length=10, default="Pending")

    def __str__(self):
        return f"Petrol Booking for {self.name} - {self.fuel_type} ({self.status})"


