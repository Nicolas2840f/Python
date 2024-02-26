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
        textoNombre.className = 'pelicula-texto pelicula-nombre z-10 text-base pt-2'; // Agregar la clase z-10 y pelicula-nombre
        textoDescripcion.className = 'pelicula-texto pelicula-descripcion z-10 pt-4 text-sm'; // Agregar la clase z-10 y pelicula-descripcion
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

function buscar() {
    // Obtener el valor ingresado por el usuario en el campo de búsqueda
    var valorBusqueda = document.querySelector('.input-busqueda').value.toLowerCase();

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
}
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
            document.body.classList.remove('overflow-hidden');
            
        } else {
            // Ocultar la película si no coincide con la búsqueda
            pelicula.style.display = 'none';
            
            document.body.classList.add('overflow-hidden');
            
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

// Agregar un evento de escucha para la tecla Enter en el input de búsqueda
document.getElementById("searchInput2").addEventListener("keypress", function(event) {
    if (event.key === "Enter") {
        event.preventDefault(); // Evitar el comportamiento predeterminado de la tecla Enter (enviar formulario)
        buscar2(); // Llamar a la función buscar() cuando se presiona Enter
    }
});


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


document.addEventListener('DOMContentLoaded', function () {
    const agregarFavoritoForms = document.querySelectorAll('.favorito-form');

    agregarFavoritoForms.forEach(form => {
        const peliculaIdInput = form.querySelector('input[name="peliculaFavorito"]');
        const usuarioIdInput = form.querySelector('input[name="usuarioFavorito"]');

        // Verificar que los inputs existan y tengan valores
        if (peliculaIdInput && usuarioIdInput && peliculaIdInput.value && usuarioIdInput.value) {
            const peliculaId = peliculaIdInput.value;
            const usuarioId = usuarioIdInput.value;

            fetch(`/favorito/verificar/${peliculaId}/${usuarioId}`)
                .then(response => response.json())
                .then(data => {
                    const botonAgregarFavorito = form.querySelector('.agregar-favorito-btn');

                    if (data.enFavoritos) {
                        botonAgregarFavorito.style.display = 'none';
                    } else {
                        botonAgregarFavorito.style.display = 'block';
                    }
                })
                .catch(error => {
                    console.error('Error al verificar favorito:', error);
                });
        } else {
            console.error('Valores de ID de película o usuario no definidos');
        }
    });
});

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

