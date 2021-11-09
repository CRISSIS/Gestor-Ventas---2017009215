from django.shortcuts import render, redirect
from django.urls import resolve
from Apps.GestorVentas.models import *

# Create your views here.

# Proyección de templates:

def vistaLogin(request):
    return render(request, "login.html")

def vistaLogout(request):
    return render(request, "login.html")

def vistaRegister(request):
    return render(request, "register.html")

def vistaAdmin(request):
    usuariosActuales =  Usuario.objects.all()
    return render(request, "admin.html", {"usuariosActuales": usuariosActuales})

def vistaVendedor(request):
    usuariosActuales =  Usuario.objects.all()
    return render(request, "vendedor.html", {"usuariosActuales": usuariosActuales})

def vistaReporte(request):
    usuariosActuales =  Usuario.objects.all()
    return render(request, "reporte.html", {"usuariosActuales": usuariosActuales})

def vistaComprador(request):
    usuariosActuales =  Usuario.objects.all()
    return render(request, "comprador.html", {"usuariosActuales": usuariosActuales})

""" def vistaDashboard(request):
    return render(request, "dashboard.html") """

# Registro de Usuario

def registrarUsuarioCompleto(request):
    nombres = request.POST['nombresC'] #basado en el "name" del input html
    apellidos = request.POST['apellidosC']
    usuario = request.POST['usuarioC']
    privilegio = request.POST['privilegioC']
    if privilegio == "Admin":
        rolElegido = Rol.objects.get(ID_Rol = "1")
    elif privilegio == "Vendedor":
        rolElegido = Rol.objects.get(ID_Rol = "2")
    else:
        rolElegido = Rol.objects.get(ID_Rol = "3")
    correo = request.POST['correoC']
    edad = request.POST['edadC']
    password = request.POST['passC']
    foto = request.POST['fotoC']
    usuarioNuevo = Usuario.objects.create(
        nombres=nombres,apellidos=apellidos,usuario=usuario,
         correo=correo, edad=edad, imagen=foto,
        estado= "Activo" , password = password, rol = rolElegido)
    return vistaAdmin(request)

def registrarUsuarioNuevo(request):
    nombres = request.POST['nombresN'] #basado en el "name" del input html
    apellidos = request.POST['apellidosN']
    usuario = request.POST['usuarioN']
    rolElegido = Rol.objects.get(ID_Rol = "2")
    correo = request.POST['correoN']
    edad = request.POST['edadN']
    password = request.POST['passN']
    foto = request.POST['fotoN']
    usuarioNuevo = Usuario.objects.create(
        nombres=nombres,apellidos=apellidos,usuario=usuario,
         correo=correo, edad=edad, imagen=foto,
        estado= "Activo" , password = password, rol = rolElegido)
    return vistaLogin(request)

def loguearUsuario(request):
    usuarioIngresado = request.POST['usuarioLog'] #basado en el "name" del input html
    passIngresada = request.POST['passLog']
    existenciaUsuario = Usuario.objects.filter(usuario = usuarioIngresado).exists()
    if existenciaUsuario :
        usuarioLocalizado = Usuario.objects.get(usuario = usuarioIngresado)
        if passIngresada == usuarioLocalizado.password:
            #se inicia sesión determinando el panel correcto a mostrar
            print(usuarioLocalizado.rol)
            print(usuarioLocalizado.rol.ID_Rol)
            if usuarioLocalizado.rol.ID_Rol == 1:
                return vistaAdmin(request)
            elif usuarioLocalizado.rol.ID_Rol == 2:
                return vistaVendedor(request)
            else:
                return vistaReporte(request)
        else:
            return vistaLogin(request)
    else:
        return vistaLogin(request)