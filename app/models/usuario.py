from app import db
from sqlalchemy.orm import relationship

class Usuario(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    nombre = db.Column(db.String(100),nullable=False)
    telefono = db.Column(db.String(45),nullable=False)
    email = db.Column(db.String(45),nullable=False)
    password = db.Column(db.String(100),nullable=False)
    rol = db.Column(db.Integer,db.ForeignKey('rol.id'))