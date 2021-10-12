#rutas o urls de la app gestor ventas

from django.urls import path
from . import views
#importamos las vistas para poder asignarlas a una url

urlpatterns = [
    path('login/', views.vistaLogin),
    path('register/', views.vistaRegister)
]