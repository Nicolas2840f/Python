//Validaciones del Código

// function compararCodigos() {
//     var resetCodeEncoded = document.getElementById("reset_code_encoded").value;
//     var userCode = document.getElementById("user_code_input").value;

//     // Decodificar el valor del input oculto
//     var decodedResetCode = atob(resetCodeEncoded);

//     if (userCode === decodedResetCode) {
//         alert("Los códigos coinciden.");
//         // Aquí puedes realizar otras acciones si los códigos coinciden
//     } else {
//         alert("Los códigos no coinciden. Inténtalo de nuevo.");
//         // Aquí puedes realizar otras acciones si los códigos no coinciden
//     }
// }
let a = document.getElementById('a')

a.addEventListener('click',(e)=>{
    let resetCodeEncoded = document.getElementById("reset_code_encoded").value.trim();
    let userCode = document.getElementById("user_code_input").value.trim();
    let decodedResetCode = atob(resetCodeEncoded);
    let span = document.getElementById("codigo");

    if (!(decodedResetCode === userCode)){
        span.classList.add('mt-4')
        span.innerHTML = "El código ingresado es inválido";
        e.preventDefault();
    }
})

