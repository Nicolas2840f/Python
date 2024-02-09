let formulario = document.forms['formulario-reset'];
const datos = {
    password: formulario.passwordUsuario,
    passwordConfirmation: formulario.passwordConfirmation
}

let validarCampoContraseña = ()=>{
    if(!(datos.password.value.length < 8 )){
        return true
    }else{
        let spanContraseña = document.getElementById('contraseñasInvalidas');
        spanContraseña.classList.add("mt-4");
        spanContraseña.innerHTML = "The password cannot be less than 8 characters";
        return false
    }
}
let validarContraseñas = () => {
    let spanContraseña = document.getElementById('contraseñasInvalidas');
    if (!(datos.password.value == datos.passwordConfirmation.value)) {
        spanContraseña.classList.add("my-2");
        spanContraseña.innerHTML = "Las Contraseñas No Coinciden";
        datos.password.classList.add('invalido');
        datos.password.classList.remove('caja');
        datos.passwordConfirmation.classList.add('invalido');
        datos.passwordConfirmation.classList.remove('caja');
        return false;
    } else {
        spanContraseña.innerHTML = "";
        spanContraseña.classList.remove("my-2");
        datos.password.classList.remove('invalido');
        datos.passwordConfirmation.classList.remove('invalido');
        return true;
    }
}

formulario.addEventListener("submit", (event) => {
    if (!(validarContraseñas() && validarCampoContraseña())) {
        event.preventDefault(); // Evitar el envío del formulario si hay errores
    }
});