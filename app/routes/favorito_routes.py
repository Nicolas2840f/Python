from flask import Blueprint,render_template,request,redirect,url_for
from app.models.favorito import Favorito
from app import db

bp = Blueprint('favorito',__name__)

@bp.route('/Favorito')
def index():
    data = Favorito.query.all()
    return render_template('favoritos/index.html',data = data)

@bp.route('/Favorito/add', methods=['GET','POST'])
def add():
    if request.method == 'POST':
        usuarios = request.form['usuarioFavorito']
        peliculas = request.form['peliculaFavorito']
        
        new_Favorito = Favorito(usuarios = usuarios,peliculas = peliculas)
        db.session.add(new_Favorito)
        db.session.commit()
        
        return redirect(url_for('favorito.index'))
    data = Favorito.query.all()
    return render_template('favoritos/add.html',data = data)

@bp.route('/Favorito/edit/<int:id>', methods=['GET','POST'])
def edit(id):
    favorito = Favorito.query.get_or_404(id)
    
    if request.method == 'POST':
        favorito.usuarios = request.form['usuariosFavorito']
        favorito.peliculas = request.form['peliculasFavorito']
        
        db.session.commit()
        
        return redirect(url_for('favorito.index'))

    return render_template('favoritos/add.html',favorito = favorito)

@bp.route('/Favorito/delete/<int:id>', methods=['GET','POST'])
def delete(id):
    favorito = Favorito.query.get_or_404(id)
    
    db.session.delete(favorito)
    db.session.commit()
        
    return redirect(url_for('favorito.index'))

