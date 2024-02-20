let formulario = document.forms['formulario-editar'];

const datos = {
    nombre: formulario.nombreUsuario,
    telefono: formulario.telefonoUsuario,
    correo: formulario.emailUsuario
}

let nombreValido = /^[a-zA-ZñÑáéíóú]+ [a-zA-ZñÑáéíóú]+ ?([a-zA-ZñÑáéíóú]+)? ?([a-zA-ZñÑáéíóú]+)? ?$/;
let correoValido = /^[a-zA-Z\.-_\d]+@[a-zA-Z]+\.(com|edu)+\.?(co|net)?$/;

let validarNombre = () => {
    let spanNombre = document.getElementById('nombreInvalido');
    if (!(datos.nombre.value).match(nombreValido)) {
        spanNombre.classList.add("my-2");
        spanNombre.innerHTML = "Nombre Inválido (Ej:Nicolás Castañeda Pardo)";
        datos.nombre.classList.add('invalido');
        datos.nombre.classList.remove('caja');
        return false;
    } else {
        spanNombre.innerHTML = "";
        spanNombre.classList.remove("my-2");
        datos.nombre.classList.remove('invalido');
        return true;
    }
}

let validarTelefono = () => {
    let spanTelefono = document.getElementById('telefonoInvalido');
    if (datos.telefono.value.length != 10) {
        spanTelefono.classList.add("my-2");
        spanTelefono.innerHTML = "Telefono Inválido (10 digitos)";
        datos.telefono.classList.add('invalido');
        datos.telefono.classList.remove('caja');
        return false;
    } else {
        spanTelefono.innerHTML = "";
        spanTelefono.classList.remove("my-2");
        datos.telefono.classList.remove('invalido');
        return true;
    }
}

let validarCorreo = () => {
    let spanCorreo = document.getElementById('correoInvalido');
    if (!(datos.correo.value).match(correoValido)) {
        spanCorreo.classList.add("my-2");
        spanCorreo.innerHTML = "Correo Inválido (Ej:ncastaneda840@gmail.com.co)";
        datos.correo.classList.add('invalido');
        datos.correo.classList.remove('caja');
        return false;
    } else {
        spanCorreo.innerHTML = "";
        spanCorreo.classList.remove("my-2");
        datos.correo.classList.remove('invalido');
        return true;
    }
}

formulario.addEventListener("submit", (event) => {
    if (!(validarNombre() && validarTelefono() && validarCorreo())) {
        event.preventDefault(); // Evitar el envío del formulario si hay errores
    }
});