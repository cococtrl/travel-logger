from django import forms
from django.forms import ModelForm
from .models import Trip

class TripForm(ModelForm):
    class Meta:
        model: Trip
        fields: ['name', 'description', 'arrival', 'departure']
