from flask import Blueprint,render_template,request,redirect,url_for
from app.models.pelicula import Pelicula
from flask_login import login_user, logout_user, login_required

from app import db 

bp = Blueprint('pelicula',__name__)

@bp.route('/Pelicula')
@login_required
def index():
    # data = Pelicula.query.all()
    return render_template('peliculas/index.html')

@bp.route('/Pelicula/add', methods=['GET','POST'])
def add():
    if request.method == 'POST':
        nombre = request.form['nombrePelicula']
        descripcion = request.form['descripcionPelicula']
        imagen = request.form['imagenPelicula']
        genero = request.form['generoPelicula']
        
        new_Pelicula = Pelicula(nombre = nombre,descripcion = descripcion,imagen = imagen,genero = genero)
        db.session.add(new_Pelicula)
        db.session.commit()
        
        return redirect(url_for('pelicula.index'))
    data = Pelicula.query.all()
    return render_template('peliculas/add.html',data = data)

@bp.route('/Pelicula/edit/<int:id>', methods=['GET','POST'])
def edit(id):
    pelicula = Pelicula.query.get_or_404(id)
    
    if request.method == 'POST':
        pelicula.nombre = request.form['nombrePelicula']
        pelicula.descripcion = request.form['descripcionPelicula']
        pelicula.imagen = request.form['imagenPelicula']
        pelicula.genero = request.form['generoPelicula']
        
        db.session.commit()
        
        return redirect(url_for('pelicula.index'))

    return render_template('peliculas/add.html',pelicula = pelicula)

@bp.route('/Pelicula/delete/<int:id>', methods=['GET','POST'])
def delete(id):
    pelicula = Pelicula.query.get_or_404(id)
    
    db.session.delete(pelicula)
    db.session.commit()
        
    return redirect(url_for('pelicula.index'))

