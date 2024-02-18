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
        usuario_id = request.form['usuarioFavorito']
        pelicula_id = request.form['peliculaFavorito']
        
        new_favorito = Favorito(usuario_id=usuario_id, pelicula_id=pelicula_id)
        db.session.add(new_favorito)
        db.session.commit()
        
    return redirect(url_for('pelicula.index'))


@bp.route('/Favorito/delete/<int:id>', methods=['POST'])
def delete(id):
    favorito_id = request.json['id']
    # Ahora puedes usar favorito_id para eliminar el favorito correspondiente de la base de datos
    favorito = Favorito.query.get_or_404(favorito_id)
    db.session.delete(favorito)
    db.session.commit()
    return redirect(url_for('favorito.index'))

