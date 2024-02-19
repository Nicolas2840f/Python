from flask import Blueprint,render_template,request,redirect,url_for,jsonify
from app.models.favorito import Favorito
from app.models.pelicula import Pelicula
from flask_login import current_user,login_required
from app import db

bp = Blueprint('favorito',__name__)
@bp.route('/Favorito')
@login_required
def index():
    if current_user.is_authenticated:
        favoritos = Favorito.query.filter_by(usuario=current_user.id).all()
        peliculas = Pelicula.query.all()
        return render_template('favoritos/index.html', favoritos=favoritos,peliculas = peliculas)
    else:
        # Manejar el caso en el que el usuario no esté autenticado
        return redirect(url_for('usuario.login'))

@bp.route('/Favorito/add', methods=['GET', 'POST'])
@login_required
def add():
    if request.method == 'POST':
        usuario = request.form['usuarioFavorito']
        pelicula= request.form['peliculaFavorito']
        
        new_favorito = Favorito(usuario = usuario, pelicula=pelicula)
        db.session.add(new_favorito)
        db.session.commit()
        
    return redirect(url_for('pelicula.index'))


@bp.route('/Favorito/delete/<int:id>', methods=['GET'])
@login_required
def delete(id):
    favorito= Favorito.query.get_or_404(id)
    
    db.session.delete(favorito)
    db.session.commit()
        
    return redirect(url_for('pelicula.index'))

@bp.route('/favorito/verificar/<int:pelicula_id>/<int:usuario_id>', methods=['GET'])
@login_required
def verificar_favorito(pelicula_id, usuario_id):
    # Buscar si la película está en la lista de favoritos del usuario
    favorito = Favorito.query.filter_by(pelicula=pelicula_id, usuario=usuario_id).first()

    if favorito:
        # Si la película está en la lista de favoritos, devolver True
        return jsonify({'enFavoritos': True})
    else:
        # Si la película no está en la lista de favoritos, devolver False
        return jsonify({'enFavoritos': False})
    
@bp.route('/favorito/delete_all/<int:id>', methods=['GET'])
@login_required
def delete_all_favoritos(id):
    # Eliminar todos los favoritos del usuario especificado
    db.session.query(Favorito).filter(Favorito.usuario == id).delete()
    db.session.commit()

    return redirect(url_for('favorito.index'))