from app import db

class Pelicula(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.String(500), nullable=False)
    imagen= db.Column(db.String(100), nullable=False)
    genero = db.Column(db.Integer, db.ForeignKey('genero.id'))
    