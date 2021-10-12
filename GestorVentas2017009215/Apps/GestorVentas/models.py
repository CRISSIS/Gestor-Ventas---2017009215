from django.db import models

# Create your models here.

class Prueba(models.Model):
    codigo = models.CharField(primary_key=True, max_length=5)
    nombre = models.CharField(max_length=50)


class Roles(models.Model):
    ID_Rol = models.CharField(primary_key=True, max_length=5)
    nombre = models.CharField(max_length=50)

class Acciones(models.Model):
    ID_Rol = models.CharField(primary_key=True, max_length=5)
    nombre = models.CharField(max_length=50)

class Bitacoras(models.Model):
    ID_Bitacora = models.CharField(primary_key=True, max_length=5)
    fecha = models.CharField(max_length=50)
    hora = models.CharField(max_length=50)
    direccion_IP = models.CharField(max_length=50)
