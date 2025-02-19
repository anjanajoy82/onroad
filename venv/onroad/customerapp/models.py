from django.db import models
from onroadapp.models import *

# Create your models here.
class MechBooking(models.Model):
    user=models.ForeignKey(Register, on_delete=models.CASCADE,null=True,related_name='user')
    mechanic=models.ForeignKey(Register, on_delete=models.CASCADE,null=True,related_name='mechanic')
    name=models.CharField(max_length=50,null=True)
    description=models.CharField(max_length=50,null=True)
    current_loc=models.URLField(max_length=255, null=True)
    vehicle_type=models.CharField(max_length=50,null=True)
    status=models.CharField(max_length=10,default="Pending")
