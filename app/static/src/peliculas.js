document.addEventListener("DOMContentLoaded", function() {
    // Obtener todos los elementos con la clase 'pelicula'
    var peliculas = document.querySelectorAll('.pelicula');

    // Iterar sobre cada película
    peliculas.forEach(function(pelicula) {
        // Obtener el nombre y la descripción de la película desde los atributos de datos
        var nombre = pelicula.dataset.nombre;
        var descripcion = pelicula.dataset.descripcion;

        // Crear un elemento de texto para mostrar el nombre y la descripción
        var textoNombre = document.createElement('div');
        var textoDescripcion = document.createElement('div');
        textoNombre.className = 'pelicula-texto pelicula-nombre z-10 text-base '; // Agregar la clase z-10 y pelicula-nombre
        textoDescripcion.className = 'pelicula-texto pelicula-descripcion z-10 text-sm'; // Agregar la clase z-10 y pelicula-descripcion
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
        pelicula.addEventListener('mouseenter', function() {
            textoNombre.style.display = 'block';
            textoDescripcion.style.display = 'block';
        });

        // Ocultar el texto cuando el mouse sale de la película
        pelicula.addEventListener('mouseleave', function() {
            textoNombre.style.display = 'none';
            textoDescripcion.style.display = 'none';
        });
    });
});

function buscar() {
    // Obtener el valor ingresado por el usuario en el campo de búsqueda
    var valorBusqueda = document.querySelector('.input-busqueda').value.toLowerCase();
    
    // Obtener todas las películas
    var peliculas = document.querySelectorAll('.pelicula');

    // Iterar sobre cada película
    peliculas.forEach(function(pelicula) {
        // Obtener el nombre de la película desde los atributos de datos
        var nombre = pelicula.dataset.nombre.toLowerCase();

        // Comprobar si el nombre de la película contiene la letra ingresada por el usuario
        if (nombre.includes(valorBusqueda)) {
            // Mostrar la película si coincide con la búsqueda
            pelicula.style.display = 'block';
        } else {
            // Ocultar la película si no coincide con la búsqueda
            pelicula.style.display = 'none';
        }
    });
}

document.addEventListener('DOMContentLoaded', function () {
    const generoElements = document.querySelectorAll('.genero');
    const peliculas = document.querySelectorAll('.pelicula');

    generoElements.forEach(genero => {
        genero.addEventListener('click', function () {
            const generoId = genero.dataset.generoId;
            // Ocultar todas las películas
            peliculas.forEach(pelicula => {
                pelicula.style.display = 'none';
            });
            // Mostrar solo las películas del género seleccionado
            const peliculasDelGenero = document.querySelectorAll(`.pelicula[data-genero="${generoId}"]`);
            peliculasDelGenero.forEach(pelicula => {
                pelicula.style.display = 'block';
            });
        });
    });
});
document.addEventListener('DOMContentLoaded', function () {
    const yearElements = document.querySelectorAll('.year');
    const peliculas = document.querySelectorAll('.pelicula');

    yearElements.forEach(year => {
        year.addEventListener('click', function () {
            // Ocultar todas las películas
            const año = year.dataset.año;
            peliculas.forEach(pelicula => {
                pelicula.style.display = 'none';
            });
            // Mostrar solo las películas del género seleccionado
            const peliculasDelYear = document.querySelectorAll(`.pelicula[data-year="${año}"]`);
            peliculasDelYear.forEach(pelicula => {
                pelicula.style.display = 'block';
            });
        });
    });
});


