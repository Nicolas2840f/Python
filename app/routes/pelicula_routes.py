from flask import Blueprint, render_template, request, redirect, url_for,session,flash
from app.models.pelicula import Pelicula
from app.models.genero import Genero
from app.models.favorito import Favorito
from flask_login import login_user, logout_user, login_required,current_user
from app import db, create_app
from werkzeug.utils import secure_filename
import os

bp = Blueprint('pelicula', __name__)


@bp.route('/Pelicula')
@login_required
def index():
    peliculas = Pelicula.query.all()
    generos = Genero.query.all()

    # Verifica si el usuario ha iniciado sesión antes de acceder a session
    if current_user.is_authenticated:
        favoritos = Favorito.query.filter_by(usuario = current_user.id).all()
    else:
        favoritos = []

    return render_template('peliculas/index.html', peliculas=peliculas, generos=generos, favoritos=favoritos)

@bp.route('/Pelicula/add', methods=['GET', 'POST'])
@login_required
def add():
    from app import create_app  # Importa dentro de la función para evitar el ciclo de importación circular
    app = create_app()
    
    if request.method == 'POST':
        nombre = request.form['nombrePelicula']
        descripcion = request.form['descripcionPelicula']
        genero = request.form['generoPelicula']
        año = request.form['añoPelicula']
        imagen = request.files['imagenPelicula']

        if imagen.filename != '':
            # Guardar la imagen en la carpeta de imágenes dentro de la carpeta 'static'
            filename = secure_filename(imagen.filename)
            imagen.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            # Guardar la ruta relativa al archivo en la base de datos
            ruta_imagen = filename
        else:
            # Si no se proporciona una imagen, muestra un mensaje de error y vuelve a la página de agregar películas
            flash('No has seleccionado una imagen válida para agregar la película', 'error')
            return redirect(url_for('pelicula.add'))

        new_Pelicula = Pelicula(nombre=nombre, descripcion=descripcion, imagen=ruta_imagen, genero=genero, año=año)
        db.session.add(new_Pelicula)
        db.session.commit()

        return redirect(url_for('pelicula.index'))

    generos = Genero.query.all()
    return render_template('peliculas/add.html',generos = generos)


@bp.route('/Pelicula/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit(id):
    from app import create_app  # Importa dentro de la función para evitar el ciclo de importación circular
    app = create_app()
    pelicula = Pelicula.query.get_or_404(id)
    
    if request.method == 'POST':
        pelicula.nombre = request.form['nombrePelicula']
        pelicula.descripcion = request.form['descripcionPelicula']
        pelicula.genero = request.form['generoPelicula']
        pelicula.año = request.form['añoPelicula']
        imagen = request.files['imagenPelicula']
        if imagen:
            # Guardar la imagen en la carpeta de imágenes dentro de la carpeta 'static'
            filename = secure_filename(imagen.filename)
            imagen.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            # Guardar la ruta relativa al archivo en la base de datos
            pelicula.imagen =  filename
        
        db.session.commit()
        
        return redirect(url_for('pelicula.index'))
    generos = Genero.query.all()
    return render_template('peliculas/edit.html', pelicula=pelicula,generos = generos)

@bp.route('/Pelicula/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete(id):
    pelicula = Pelicula.query.get_or_404(id)
    
    db.session.delete(pelicula)
    db.session.commit()
        
    return redirect(url_for('pelicula.index'))

@bp.route('/Pelicula/view/<int:id>', methods=['GET', 'POST'])
@login_required
def view(id):
    pelicula = Pelicula.query.get_or_404(id)
    generos = Genero.query.all()
    return render_template('peliculas/view.html',pelicula = pelicula,generos = generos)