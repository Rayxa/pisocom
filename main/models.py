from django.db import models
from django.utils import timezone

class IntegerRangeField(models.IntegerField):
    def __init__(self, verbose_name=None, name=None, min_value=None, max_value=None, **kwargs):
        self.min_value, self.max_value = min_value, max_value
        models.IntegerField.__init__(self, verbose_name, name, **kwargs)
    def formfield(self, **kwargs):
        defaults = {'min_value': self.min_value, 'max_value':self.max_value}
        defaults.update(kwargs)
        return super(IntegerRangeField, self).formfield(**defaults)

class Direccion(models.Model):
    usuario = models.ForeignKey('auth.User')
    pais = models.CharField(max_length=30)
    comunidadAutonoma = models.CharField(max_length=30)
    provincia = models.CharField(max_length=30)
    codigoPostal = models.IntegerField()
    calle = models.CharField(max_length=30)
	
    def __str__(self):
        return self.comunidadAutonoma + ", " + self.provincia + ", " + self.calle	

			
class Casa(models.Model):
    propietario = models.ForeignKey('auth.User')
    direccion = models.ForeignKey(Direccion, on_delete=models.CASCADE)
    descripcion = models.TextField()
    numHabitaciones = IntegerRangeField(min_value=1, max_value=20)
    habitacionesDisponibles = IntegerRangeField(min_value=0, max_value=20)
    precio = IntegerRangeField(min_value=0, max_value=20)
    gastosIncluidos = models.BooleanField(default=False)
    diaCreacion = models.DateTimeField(
            default=timezone.now)

    def __str__(self):
        return self.propietario + ", " + self.descripcion