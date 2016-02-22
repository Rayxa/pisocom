from django import forms

from .models import casa, descripcion

class casaForm(forms.ModelForm):

    class Meta:
        model = casa
        fields = ('numHabitaciones', 'precio','habitacionesDisponibles','gastosIncluidos','fotos','descripcion',)