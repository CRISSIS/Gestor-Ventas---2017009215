from django.contrib import admin
#importamos los modelos
from .models import *

# Register your models here.

"""
Agregamos nuestros modelos para poder
configurarlos en el panel admin
"""
admin.site.register(Prueba)
admin.site.register(Roles)
admin.site.register(Acciones)
admin.site.register(Bitacoras)
