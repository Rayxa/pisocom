from django import forms
from .models import Casa, Direccion

class formCrearCasa(forms.ModelForm):

    class Meta:
        model = Casa
        fields = ('propietario', 'direccion', 'descripcion', 'numHabitaciones', 'habitacionesDisponibles', 
        'precio', 'gastosIncluidos',)

    #class Meta:
    #    model = Direccion
    #    fields = ('pais', 'comunidadAutonoma', 'provincia', 'codigoPostal',)