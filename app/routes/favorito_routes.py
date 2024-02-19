from flask import Blueprint,render_template,request,redirect,url_for,jsonify
from app.models.favorito import Favorito
from app import db

bp = Blueprint('favorito',__name__)

@bp.route('/Favorito')
def index():
    data = Favorito.query.all()
    return render_template('favoritos/index.html',data = data)

@bp.route('/Favorito/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        usuario = request.form['usuarioFavorito']
        pelicula= request.form['peliculaFavorito']
        
        new_favorito = Favorito(usuario = usuario, pelicula=pelicula)
        db.session.add(new_favorito)
        db.session.commit()
        
    return redirect(url_for('pelicula.index'))


@bp.route('/Favorito/delete/<int:id>', methods=['GET'])
def delete(id):
    favorito= Favorito.query.get_or_404(id)
    
    db.session.delete(favorito)
    db.session.commit()
        
    return redirect(url_for('pelicula.index'))

@bp.route('/favorito/verificar/<int:pelicula_id>/<int:usuario_id>', methods=['GET'])
def verificar_favorito(pelicula_id, usuario_id):
    # Buscar si la película está en la lista de favoritos del usuario
    favorito = Favorito.query.filter_by(pelicula=pelicula_id, usuario=usuario_id).first()

    if favorito:
        # Si la película está en la lista de favoritos, devolver True
        return jsonify({'enFavoritos': True})
    else:
        # Si la película no está en la lista de favoritos, devolver False
        return jsonify({'enFavoritos': False})