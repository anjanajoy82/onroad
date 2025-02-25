from django import forms
from .models import *
from django.core.exceptions import ValidationError
import re
from django.core.validators import RegexValidator

class FuelForm(forms.ModelForm):
    
    class Meta:
        model=FuelDetails
        fields=['fuel_name','fuel_price']
        widgets={
            'fuel_name':forms.TextInput(attrs={'id':'fuel_name','name':'fuel_name'}),
            'fuel_price':forms.TextInput(attrs={'id':'fuel-price','name':'fuel_price'}),
            
        }
        labels={
            'fuel_name':'FUEL NAME',
            'fuel_price':'FUEL PRICE',

            
        }
        help_texts={
            'username':None
        }
