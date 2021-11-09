#rutas o urls de la app gestor ventas

from django.urls import path
from . import views
#importamos las vistas para poder asignarlas a una url

urlpatterns = [
    path('login/', views.vistaLogin),
    path('dirigirRegistroUsuario/', views.vistaRegister),
    #registros de usuario por ruta:
    path('registrarUsuarioCompleto/', views.registrarUsuarioCompleto),
    path('registrarUsuarioNuevo/', views.registrarUsuarioNuevo),
    path('loguearUsuario/', views.loguearUsuario),

    path('comprador/', views.vistaComprador),
    path('vendedor/', views.vistaVendedor),
    path('reporte/', views.vistaReporte),
    path('soyadmin/', views.vistaAdmin),

    path('logout/', views.vistaLogout, name='logout'),
]