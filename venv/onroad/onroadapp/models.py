from django.db import models
from django.contrib.auth.models import AbstractUser


class Register(AbstractUser):
    usertype=models.CharField(max_length=50,default="admin")
    contact=models.IntegerField(null=True)
    image=models.ImageField(upload_to='uploads/',null=True)
    licenseno=models.CharField(max_length=15,null=True)
    location = models.URLField(max_length=255, null=True)
    idproof=models.ImageField(upload_to='proofs/',null=True)
    experience=models.IntegerField(null=True)
    specialization=models.CharField(max_length=50,null=True,blank=True)
    availability=models.BooleanField(default=True)
    licence_verified=models.BooleanField(default=False)
    pump_name=models.CharField(max_length=50,null=True)
    place=models.CharField(max_length=50,null=True)
    is_approved= models.BooleanField(default=True)
    pump_id=models.IntegerField(null=True)
    


# Create your models here.
class Reset(models.Model):
    otp = models.CharField(max_length=6, null=True)
    user = models.ForeignKey(Register, on_delete=models.CASCADE,null=True)
    otp_created_at = models.DateTimeField(auto_now_add =True)

