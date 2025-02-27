from django.db import models
from onroadapp.models import *

class FuelDetails(models.Model):
    petrol_pump = models.ForeignKey(Register, on_delete=models.CASCADE, related_name="fuel_details")
    fuel_name = models.CharField(max_length=50)
    fuel_price = models.DecimalField(max_digits=6, decimal_places=2)
     
    

    def __str__(self):
        return f"{self.fuel_name} - {self.petrol_pump.first_name} {self.petrol_pump.last_name}"


