

var mainApp = new Vue({
    delimiters: ['${', '}'], /*Cambiamos el delimitador para que no de problema con jinga2 Django */
	el: '#main',
	data: {
    //#region DATA
      estadoVisualizadores: { /*estadosa predeterminados */
        estadoSegmento1: true,
        estadoSegmento2: false,
        estadoSegmento3: false,
      },
      estiloActual:{
        activo: "opcionesMenu",
        inactivo: "opcionesMenuDesactivadas"
      }
    //#endregion DATA
    },
    methods:{
        //#region METHODS
        activarVisorSegmento1: function(){
            this.estadoVisualizadores.estadoSegmento1 = true;
            this.estadoVisualizadores.estadoSegmento2 = false;
            this.estadoVisualizadores.estadoSegmento3 = false;
        },
        activarVisorSegmento2: function(){
            this.estadoVisualizadores.estadoSegmento1 = false;
            this.estadoVisualizadores.estadoSegmento2 = true;
            this.estadoVisualizadores.estadoSegmento3 = false;
        },
        activarVisorSegmento3: function(){
            this.estadoVisualizadores.estadoSegmento1 = false;
            this.estadoVisualizadores.estadoSegmento2 = false;
            this.estadoVisualizadores.estadoSegmento3 = true;
        }
      //#endregion METHODS
    }
})



//#region Control de Fecha y Hora

function actualizarFecha(){
  let controladorTiempo = new Date();
  let fecha = controladorTiempo.getDate() + '/' + (controladorTiempo.getMonth()+1) + '/' + controladorTiempo.getFullYear();
  document.getElementById("visorFechaActual").innerHTML = fecha;
}

function actualizarHora(){
  let controladorTiempo = new Date();
  let hora = String(controladorTiempo.getHours()).padStart(2, "0") + ':' + String(controladorTiempo.getMinutes()).padStart(2, "0")  + ':' + String(controladorTiempo.getSeconds()).padStart(2, "0");
  document.getElementById("visorHoraActual").innerHTML = hora;
}

function ejecutarReloj(){
  setInterval(actualizarHora, 1000);
}
 

//#endregion Control de Fecha y Hora

//#region control de actividad/inactividad de los botones

function activarBoton(boton){
    boton.disabled = false;
}

function desactivarBoton(boton){
    boton.disabled = true;
}


//#endregion control de actividad/inactividad de los botones

//#region funciones de botones

function permitirEdicionPerfil(){
    desactivarBoton(document.getElementById('botonEdicionPerfil'));
    activarBoton(document.getElementById('botonGuardado'));
    desbloquearInputsEdicion();
    alert("Puede editar su información personal");
}

function permitirGuardarCambiosPerfil(){
    activarBoton(document.getElementById('botonEdicionPerfil'));
    desactivarBoton(document.getElementById('botonGuardado'));
    bloquearInputsEdicion();
    alert("Cambios guardados");
}

function verificacionCierreSesion(){
    /*Si el boton de guardado no está bloqueado significa que 
    no se han guardado los datos, se debe impedir el cierre de sesión*/
     if(document.getElementById('botonGuardado').disabled == false){
        alert("No puede cerrar sesión sin guardar sus cambios de perfil");
    } else{
        //se cierra la sesión
        alert("Cerrando Sesión...");
        //location.href="{% url 'logout' %}";
    } 
}

function accionarVisorPass(){
    /*Si se quiere ver la contraseña el input se volverá tipo texto,
     y si es texto se volverá tipo password para ocultarla*/
    let inputPass = document.getElementById('inputPass');
    if(inputPass.type == "text"){
        inputPass.type = "password";
    }else{
        inputPass.type = "text";
    }
}

function desbloquearInputsEdicion(){
    //recolectamos todos los inputs a los que se les dará permiso para su edición
    let listaInputs = document.getElementsByClassName('editable');
    //para cada uno de ellos le quitamos la propiedad readonly
    for(let numinput = 0; numinput < listaInputs.length; numinput++){
        listaInputs[numinput].removeAttribute("readonly"  , false);
        console.log(listaInputs[numinput]);
    }
}

function bloquearInputsEdicion(){
    //recolectamos todos los inputs a los que se les dará permiso para su edición
    let listaInputs = document.getElementsByClassName('editable');
    //para cada uno de ellos le quitamos la propiedad readonly
    for(let numinput = 0; numinput < listaInputs.length; numinput++){
        listaInputs[numinput].setAttribute("readonly" , "readonly" , false);
        console.log(listaInputs[numinput]);
    }
}


//#endregion funciones de botones

//#region Asignación de funciones a botones:

document.getElementById('botonEdicionPerfil').addEventListener("click", permitirEdicionPerfil);
document.getElementById('botonGuardado').addEventListener("click", permitirGuardarCambiosPerfil);
document.getElementById('controladorSesion').addEventListener("click", verificacionCierreSesion);
document.getElementById('visorPass').addEventListener("click", accionarVisorPass);

//#endregion Asignación de funciones a botones:

//#region Ejecución de Funciones
actualizarFecha();
ejecutarReloj();

//#endregion Ejecución de Funciones


