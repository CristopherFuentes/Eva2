from django.db import models


# Create your models here.

class Paciente(models.Model):
    nombre = models.CharField(max_length=15)
    rut = models.CharField(max_length=15)
    telefono = models.CharField(max_length=15)
    correo = models.EmailField(max_length=50)
    edad = models.IntegerField()
    direccion = models.CharField(max_length=100)
