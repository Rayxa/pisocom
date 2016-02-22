from django import forms
from django.forms.widgets import SelectDateWidget
from datetime import datetime

from .models import casa

class casaForm(forms.ModelForm):

    class Meta:
        model = casa
        fields = ('numHabitaciones','author','precio',)