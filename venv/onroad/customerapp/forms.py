from django import forms
from .models import *
from django.core.exceptions import ValidationError
import re
from django.core.validators import RegexValidator

class MechForm(forms.ModelForm):
    
    class Meta:
        model=MechBooking
        fields=['name','description','current_loc','vehicle_type',]
        widgets={
            'name':forms.TextInput(attrs={'id':'name','name':'name'}),
            'description':forms.TextInput(attrs={'id':'description','name':'description'}),
            'current_loc':forms.URLInput(attrs={'id':'current_loc','name':'current_loc','placeholder': 'Location URL '}),
            'vehicle_type':forms.TextInput(attrs={'id':'vehicle_type','name':'vehicle_type'}),
        }
        labels={
            'name':'NAME',
            'description':'DESCRIPTION',
            'current_loc':'CURRENT LOCATION',
            'vehicle_type':'VEHICLE TYPE',
            
        }
        help_texts={
            'username':None
        }