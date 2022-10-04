from django.db import models
from datetime import datetime

# Create your models here.

class Familia(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    parentezco = models.CharField(max_length=30)
    anio_nacimiento = models.IntegerField()
    edad = models.IntegerField()
    fecha_registro = models.DateTimeField()
    

    ...
