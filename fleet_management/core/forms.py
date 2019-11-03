from django import forms
from .models import *

class DateInput(forms.DateInput):
    input_type = 'date'

class ReservationForm(forms.ModelForm):

    class Meta:
        model = Reservation
        fields = ['rent_from','rent_to',]
        widgets = {
            'rent_from': DateInput(),
            'rent_to': DateInput(),
        }