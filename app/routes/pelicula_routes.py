from flask import Blueprint, render_template, request, redirect, url_for
from app.models.pelicula import Pelicula
from flask_login import login_user, logout_user, login_required
from app import db, create_app
from werkzeug.utils import secure_filename
import os

bp = Blueprint('pelicula', __name__)

@bp.route('/Pelicula')
@login_required
def index():
    peliculas = Pelicula.query.all()  # Obtén todas las películas desde la base de datos
    return render_template('peliculas/index.html', peliculas=peliculas)  # Pasa la lista de películas a la plantilla


@bp.route('/Pelicula/add', methods=['GET', 'POST'])
def add():
    from app import create_app  # Importa dentro de la función para evitar el ciclo de importación circular
    app = create_app()
    if request.method == 'POST':
        nombre = request.form['nombrePelicula']
        descripcion = request.form['descripcionPelicula']
        genero = request.form['generoPelicula']
        
        # Manejo del archivo de imagen
        imagen = request.files['imagenPelicula']
        if imagen:
            # Guardar la imagen en la carpeta de imágenes dentro de la carpeta 'static'
            filename = secure_filename(imagen.filename)
            imagen.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            # Guardar la ruta relativa al archivo en la base de datos
            ruta_imagen = os.path.join('static','imagenes', 'Peliculas', filename)
        else:
            # Si no se proporciona una imagen, asigna un valor predeterminado o muestra un mensaje de error
            ruta_imagen = 'static/Peliculas/default.jpg'  # o muestra un mensaje de error
        
        new_Pelicula = Pelicula(nombre=nombre, descripcion=descripcion, imagen=ruta_imagen, genero=genero)
        db.session.add(new_Pelicula)
        db.session.commit()
        
        return redirect(url_for('pelicula.index'))
    return render_template('peliculas/add.html')


@bp.route('/Pelicula/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    from app import create_app  # Importa dentro de la función para evitar el ciclo de importación circular
    app = create_app()
    pelicula = Pelicula.query.get_or_404(id)
    
    if request.method == 'POST':
        pelicula.nombre = request.form['nombrePelicula']
        pelicula.descripcion = request.form['descripcionPelicula']
        pelicula.imagen = request.form['imagenPelicula']
        pelicula.genero = request.form['generoPelicula']
        
        db.session.commit()
        
        return redirect(url_for('pelicula.index'))

    return render_template('peliculas/add.html', pelicula=pelicula)

@bp.route('/Pelicula/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
    from app import create_app  # Importa dentro de la función para evitar el ciclo de importación circular
    app = create_app()
    pelicula = Pelicula.query.get_or_404(id)
    
    db.session.delete(pelicula)
    db.session.commit()
        
    return redirect(url_for('pelicula.index'))
