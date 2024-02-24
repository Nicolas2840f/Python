document.addEventListener("DOMContentLoaded", function () {
    // Obtener todos los elementos con la clase 'pelicula'
    var peliculas = document.querySelectorAll('.pelicula');

    // Iterar sobre cada película
    peliculas.forEach(function (pelicula) {
        // Obtener el nombre y la descripción de la película desde los atributos de datos
        var nombre = pelicula.dataset.nombre;
        var descripcion = pelicula.dataset.descripcion;

        // Crear un elemento de texto para mostrar el nombre y la descripción
        var textoNombre = document.createElement('div');
        var textoDescripcion = document.createElement('div');
        textoNombre.className = 'pelicula-texto pelicula-nombre z-10 text-base mt-2'; // Agregar la clase z-10 y pelicula-nombre
        textoDescripcion.className = 'pelicula-texto pelicula-descripcion z-10 mt-4 text-sm'; // Agregar la clase z-10 y pelicula-descripcion
        textoNombre.textContent = nombre;
        textoDescripcion.textContent = descripcion;
        textoNombre.style.color = 'white'; // Establecer el color de texto blanco
        textoDescripcion.style.color = 'white'; // Establecer el color de texto blanco

        // Agregar el elemento de texto al contenedor de la película
        pelicula.querySelector('.pelicula-imagen').appendChild(textoNombre);
        pelicula.querySelector('.pelicula-imagen').appendChild(textoDescripcion);

        // Ocultar el texto inicialmente
        textoNombre.style.display = 'none';
        textoDescripcion.style.display = 'none';

        // Mostrar el texto cuando el mouse entra en la película
        pelicula.addEventListener('mouseenter', function () {
            textoNombre.style.display = 'block';
            textoDescripcion.style.display = 'block';
        });

        // Ocultar el texto cuando el mouse sale de la película
        pelicula.addEventListener('mouseleave', function () {
            textoNombre.style.display = 'none';
            textoDescripcion.style.display = 'none';
        });
    });
});

function buscar2() {
    // Obtener el valor ingresado por el usuario en el campo de búsqueda
    var valorBusqueda = document.querySelector('.input-busqueda2').value.toLowerCase();

    // Obtener todas las películas
    var peliculas = document.querySelectorAll('.pelicula');
    var coincidenciasEncontradas = false;
    var contenedorPeliculas = document.getElementById('pelicula-container')

    // Iterar sobre cada película
    peliculas.forEach(function (pelicula) {
        // Obtener el nombre de la película desde los atributos de datos
        var nombre = pelicula.dataset.nombre.toLowerCase();

        // Comprobar si el nombre de la película contiene la letra ingresada por el usuario
        if (nombre.includes(valorBusqueda)) {
            // Mostrar la película si coincide con la búsqueda
            pelicula.style.display = 'block';
            coincidenciasEncontradas = true;
            
        } else {
            // Ocultar la película si no coincide con la búsqueda
            pelicula.style.display = 'none';
            
        }
    });

    var mensajeNoCoincidencias = document.getElementById("mensajeNoCoincidencias");
    if (!coincidenciasEncontradas) {
        mensajeNoCoincidencias.style.display = "flex";
        contenedorPeliculas.style.display = 'none'
    } else {
        mensajeNoCoincidencias.style.display = "none";
        contenedorPeliculas.style.display = 'flex'
    }
    // Ocultar el menú desplegable después de la búsqueda
    document.getElementById("check").checked = false;
}
document.addEventListener('DOMContentLoaded', function () {
    var checkbox = document.getElementById('check');
    checkbox.addEventListener('change', function () {
        if (checkbox.checked) {
            document.body.classList.add('overflow-hidden');
        } else {
            document.body.classList.remove('overflow-hidden');
        }
    });
});
