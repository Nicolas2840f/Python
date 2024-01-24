from app import db
from sqlalchemy.orm import relationship

class Favorito(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.Integer, db.ForeignKey('usuario.id'))
    pelicula = db.Column(db.Integer, db.ForeignKey('pelicula.id'))
    