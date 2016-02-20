# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-20 17:29
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Casa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField()),
                ('numHabitaciones', models.IntegerField()),
                ('habitacionesDisponibles', models.IntegerField()),
                ('precio', models.IntegerField()),
                ('gastosIncluidos', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Direccion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pais', models.CharField(max_length=30)),
                ('comunidadAutonoma', models.CharField(max_length=30)),
                ('provincia', models.CharField(max_length=30)),
                ('codigoPostal', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='casa',
            name='direccion',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.Direccion'),
        ),
    ]
