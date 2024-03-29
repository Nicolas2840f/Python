// Validaciones Registro de Usuario

let formulario = document.forms['formulario-registro'];

const datos = {
    nombre: formulario.nombreUsuario,
    telefono: formulario.telefonoUsuario,
    correo: formulario.emailUsuario,
    password: formulario.passwordUsuario,
    passwordConfirmation: formulario.passwordConfirmation
}

let nombreValido = /^[a-zA-ZñÑáéíóú]+ [a-zA-ZñÑáéíóú]+ ?([a-zA-ZñÑáéíóú]+)? ?([a-zA-ZñÑáéíóú]+)? ?$/;
let correoValido = /^[a-zA-Z\.-_\d]+@[a-zA-Z]+\.(com|edu)+\.?(co|net)?$/;

let validarNombre = () => {
    let spanNombre = document.getElementById('nombreInvalido');
    if (!(datos.nombre.value).match(nombreValido)) {
        spanNombre.classList.add("my-0.5");
        spanNombre.innerHTML = "Nombre Inválido (Ej:Nicolás Castañeda)";
        datos.nombre.classList.add('invalido');
        datos.nombre.classList.remove('caja');
        return false;
    } else {
        spanNombre.innerHTML = "";
        spanNombre.classList.remove("my-0.5");
        datos.nombre.classList.remove('invalido');
        return true;
    }
}

let validarTelefono = () => {
    let spanTelefono = document.getElementById('telefonoInvalido');
    if (datos.telefono.value.length != 10) {
        spanTelefono.classList.add("my-0.5");
        spanTelefono.innerHTML = "Telefono Inválido (10 digitos)";
        datos.telefono.classList.add('invalido');
        datos.telefono.classList.remove('caja');
        return false;
    } else {
        spanTelefono.innerHTML = "";
        spanTelefono.classList.remove("my-0.5");
        datos.telefono.classList.remove('invalido');
        return true;
    }
}

let validarCorreo = () => {
    let spanCorreo = document.getElementById('correoInvalido');
    if (!(datos.correo.value).match(correoValido)) {
        spanCorreo.classList.add("my-0.5");
        spanCorreo.innerHTML = "Correo Inválido";
        datos.correo.classList.add('invalido');
        datos.correo.classList.remove('caja');
        return false;
    } else {
        spanCorreo.innerHTML = "";
        spanCorreo.classList.remove("my-0.5");
        datos.correo.classList.remove('invalido');
        return true;
    }
}
let validarCampoContraseña = ()=>{
    if(!(datos.password.value.length < 8 )){
        return true
    }else{
        let spanContraseña = document.getElementById('contraseñasInvalidas');
        spanContraseña.classList.add("my-0.5");
        spanContraseña.innerHTML = "Contraseña Inválida";
        return false
    }
}

let validarContraseñas = () => {
    let spanContraseña = document.getElementById('contraseñasInvalidas');
    if (!(datos.password.value == datos.passwordConfirmation.value)) {
        spanContraseña.classList.add("my-0.5");
        spanContraseña.innerHTML = "Las Contraseñas No Coinciden";
        datos.password.classList.add('invalido');
        datos.password.classList.remove('caja');
        datos.passwordConfirmation.classList.add('invalido');
        datos.passwordConfirmation.classList.remove('caja');
        return false;
    } else {
        spanContraseña.innerHTML = "";
        spanContraseña.classList.remove("my-0.5");
        datos.password.classList.remove('invalido');
        datos.passwordConfirmation.classList.remove('invalido');
        return true;
    }
}



formulario.addEventListener("submit", (event) => {
    if (!(validarNombre() && validarTelefono() && validarCorreo() && validarContraseñas() && validarCampoContraseña())) {
        event.preventDefault(); // Evitar el envío del formulario si hay errores
    }
});

