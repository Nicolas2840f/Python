from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from app import db

class Usuario(db.Model,UserMixin):
    id = db.Column(db.Integer,primary_key=True)
    nombre = db.Column(db.String(100),nullable=False)
    telefono = db.Column(db.String(45),nullable=False)
    email = db.Column(db.String(45),nullable=False)
    password = db.Column(db.String(100),nullable=False)
    rol = db.Column(db.Integer,db.ForeignKey('rol.id'))