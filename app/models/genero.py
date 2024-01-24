from app import db
from sqlalchemy.orm import relationship

class Genero(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.String(45), nullable=False)
    