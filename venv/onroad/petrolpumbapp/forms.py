from django import forms
from .models import *
from django.core.exceptions import ValidationError
import re
from django.core.validators import RegexValidator

class FuelForm(forms.ModelForm):
    
    class Meta:
        model=FuelDetails
        fields=['fuel_name','fuel_types','fuel_price','image']
        widgets={
            'fuel_name':forms.TextInput(attrs={'id':'fuel_name','name':'fuel_name'}),
            'fuel_types':forms.TextInput(attrs={'id':'fuel-types','name':'types'}),
            'fuel_price':forms.NumberInput(attrs={'id':'fuel-price','name':'fuel_price'}),
            'image':forms.FileInput(attrs={'id':'image','name':'image'}),
            
        }
        labels={
            'fuel_name':'FUEL NAME',
            'fuel_types':'FUEL TYPES',
            'fuel_price':'FUEL PRICE',
            'image':'IMAGE',

            
        }
        help_texts={
            'username':None
        }