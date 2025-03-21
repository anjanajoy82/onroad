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
            'description':forms.TextInput(attrs={'id':'description','name':'description','size':80, 'placeholder': 'Describe the issue in detail'}),
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

class PetrolForm(forms.ModelForm):
    
    class Meta:
        model=PetrolBooking
        fields=['name','description','current_loc','vehicle_type','fuel_type','fuel_quantity','urgency']
        widgets={
            'name':forms.TextInput(attrs={'id':'name','name':'name'}),
            'description':forms.TextInput(attrs={'id':'description','name':'description','size':80, 'placeholder': 'Describe the issue in detail'}),
            'current_loc':forms.URLInput(attrs={'id':'current_loc','name':'current_loc','placeholder': 'Location URL '}),
            'vehicle_type':forms.TextInput(attrs={'id':'vehicle_type','name':'vehicle_type'}),
            'fuel_type':forms.TextInput(attrs={'id':'fuel_type','name':'fuel_type'}),
           
            'fuel_quantity':forms.TextInput(attrs={'id':'fuel_quantity','name':'fuel_quantity'}),
            'urgency':forms.TextInput(attrs={'id':'urgency','name':'urgency'}),
        }
        labels={
            'name':'NAME',
            'description':'DESCRIPTION',
            'current_loc':'CURRENT LOCATION',
            'vehicle_type':'VEHICLE TYPE',
            'fuel_type':'FUEL TYPE',
            
            'fuel_quantity':'FUEL QUANTITY',
            'urgency':'URGENCY',


            
        }
        help_texts={
            'username':None
        }



class MechFeedbackForm(forms.ModelForm):
    class Meta:
        model = MechFeedback
        fields = ['message', 'rating']
        widgets = {
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter your feedback'}),
            'rating': forms.Select(attrs={'class': 'form-control'}),
        }

class PetrolFeedbackForm(forms.ModelForm):
    class Meta:
        model = PetrolFeedback
        fields = ['message', 'rating']
        widgets = {
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter your feedback'}),
            'rating': forms.Select(attrs={'class': 'form-control'}),
        }