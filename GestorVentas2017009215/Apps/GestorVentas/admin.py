from django.contrib import admin
#importamos los modelos
from .models import Prueba

# Register your models here.

"""
Agregamos nuestros modelos para poder
configurarlos en el panel admin
"""
admin.site.register(Prueba)
