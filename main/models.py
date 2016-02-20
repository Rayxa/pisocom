from django.db import models
from django.utils import timezone


class Direccion(models.Model):
    pais = models.CharField(max_length=30)
    comunidadAutonoma = models.CharField(max_length=30)
    provincia = models.CharField(max_length=30)
    codigoPostal = models.IntegerField()
	

			
class Casa(models.Model):
    propietario = models.ForeignKey('auth.User')
    direccion = models.ForeignKey(Direccion, on_delete=models.CASCADE)
    descripcion = models.TextField()
    numHabitaciones = models.IntegerField()
    habitacionesDisponibles = models.IntegerField()
    precio = models.IntegerField()
    gastosIncluidos = models.BooleanField(default=False)
    diaCreacion = models.DateTimeField(
            default=timezone.now)

			