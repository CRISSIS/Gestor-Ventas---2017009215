from django.db import models

# Create your models here.

class Rol(models.Model):
    opciones_rol = (
        ('Admin', 'Admin'),
        ('Vendedor', 'Vendedor'),
        ('Reporte', 'Reporte'),
    )
    ID_Rol = models.AutoField(primary_key=True)
    nombre_rol = models.CharField(max_length=15, choices=opciones_rol)

class Accion(models.Model):
    opciones_accion = (
        ('Edicion_Perfil', 'Edicion_Perfil'),
        ('Crear_Usuario', 'Crear_Usuario'),
        ('Activar_Usuario', 'Activar_Usuario'),
        ('Punto_Venta', 'Punto_Venta'),
    )
    ID_Accion = models.AutoField(primary_key=True)
    nombre_Accion = models.CharField(max_length=30, choices=opciones_accion)

class Usuario(models.Model):
    ID_Usuario = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    usuario = models.CharField(max_length=50)
    correo = models.EmailField( blank = False, null = False)
    edad = models.PositiveIntegerField(default = 18)
    imagen = models.ImageField(upload_to='images/',max_length=255,null = True,blank = True)
    opciones_estado = (
        ('Activo', 'Activo'),
        ('Bloqueado', 'Bloqueado'),
    )
    estado = models.CharField(max_length=100,choices=opciones_estado)
    password = models.CharField(max_length=50)
    rol = models.ForeignKey( Rol, default=1,on_delete=models.CASCADE) 
    