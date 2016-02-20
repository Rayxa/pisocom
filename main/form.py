from django import forms
from .models import Casa, Direccion

class formDireccion(forms.ModelForm):

    class Meta:
        model = Direccion
        fields = ('pais', 'comunidadAutonoma', 'provincia', 'codigoPostal',)
		


		
class formCrearCasa(forms.ModelForm):

    class Meta:
        model = Casa
        fields = ('direccion', 'descripcion', 'numHabitaciones', 'habitacionesDisponibles', 
        'precio', 'gastosIncluidos',)