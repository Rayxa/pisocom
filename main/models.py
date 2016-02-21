from django.db import models

# Profile with information about a user
class Profile(models.Model):

    GENDER_CHOICES = (
        ('', 'Sin especificar'),
        ('H', 'Hombre'),
        ('M', 'Mujer'),
    )

    OCUPATION_CHOICES = (
        ('', 'Sin especificar'),
        ('E', 'Estudiante'),
        ('T', 'Trabajador'),
    )

    PET_CHOICES = (
        ('', 'Ninguna'),
        ('P', 'Perro'),
        ('G', 'Gato'),
        ('O', 'Otros'),
    )

    user = models.OneToOneField('auth.User', models.CASCADE)

    firstName = models.CharField(max_length=35, blank=True, verbose_name='Nombre')
    lastName = models.CharField(max_length=35, blank=True, verbose_name='Apellidos')
    telephone = models.CharField(max_length=15, blank=True, verbose_name='Número de teléfono')
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True, verbose_name="Sexo")

    birthdate = models.DateField(blank=True, null=True, verbose_name="Fecha de nacimiento")
    ocupation = models.CharField(max_length=1, choices=OCUPATION_CHOICES, blank=True, verbose_name="Ocupación")
    description = models.TextField(blank=True, verbose_name="Descripción")

    pet = models.CharField(max_length=1, choices=PET_CHOICES, blank=True, verbose_name='Mascota')
    isSmoker = models.BooleanField(default=False, verbose_name='Fumador')
    lookingIn = models.CharField(max_length=35, blank=True, verbose_name="Ciudad en la que buscas piso")

    # photo = models.ImageField(upload_to='/data/photos/', verbose_name='Una foto tuya')

    def __str__(self):
        return 'Perfil de ' + self.user.username

    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfiles'
