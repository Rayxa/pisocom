from django.db import models
from django.utils import timezone

class descripcion(models.Model):
    pais = models.CharField(max_length=20)
    comunidadAutonoma = models.CharField(max_length=20)
    provincia = models.CharField(max_length=20)
    codigoPostal = models.IntegerField()
    ciudad = models.CharField(max_length=20)

    def __str__(self):
        return self.pais


class casa(models.Model):
    author = models.ForeignKey('auth.User')
    numHabitaciones = models.IntegerField(default=1)
    precio = models.IntegerField()
    habitacionesDisponibles = models.IntegerField(default=1)
    gastosIncluidos = models.BooleanField(default=False)
    descripcion = models.OneToOneField(descripcion)
    #fotos = models.ImageField()
    fotos = models.CharField(max_length=200)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title