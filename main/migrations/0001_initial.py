# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.utils.timezone
import main.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Casa',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('descripcion', models.TextField()),
                ('numHabitaciones', main.models.IntegerRangeField()),
                ('habitacionesDisponibles', main.models.IntegerRangeField()),
                ('precio', main.models.IntegerRangeField()),
                ('gastosIncluidos', models.BooleanField(default=False)),
                ('diaCreacion', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Direccion',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('pais', models.CharField(max_length=30)),
                ('comunidadAutonoma', models.CharField(max_length=30)),
                ('provincia', models.CharField(max_length=30)),
                ('codigoPostal', models.IntegerField()),
                ('calle', models.CharField(max_length=30)),
                ('usuario', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='casa',
            name='direccion',
            field=models.ForeignKey(to='main.Direccion'),
        ),
        migrations.AddField(
            model_name='casa',
            name='propietario',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
