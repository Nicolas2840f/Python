
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

