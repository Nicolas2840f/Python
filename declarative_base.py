from sqlalchemy import create_engine, Column, Integer, String, Sequence,ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,relationship


Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, Sequence('usuario_id_seq'), primary_key=True)
    nombre = Column(String(100))
    telefono = Column(String(45))
    email = Column(String(45))
    password = Column(String(100))
    roles_id = Column(Integer, ForeignKey('roles.id'))
    roles = relationship('Roles',secondary='usuario_rol', cascade='all,delete,delete-orphan')

class Rol(Base):
    __tablename__ = 'roles'
    id = Column(Integer,  primary_key=True)
    nombre = Column(String(100))

class Pelicula(Base):
    __tablename__ = 'peliculas'
    id = Column(Integer,primary_key=True)
    nombre = Column(String(100))
    descripcion = Column(String(200))
    imagenes = Column(String(200))
    generos_id = Column(Integer,ForeignKey('generos.id'))
    generos = relationship('generos',secondary='pelicula_genero',cascade='all,delete,delete-orphan')

class Genero(Base):
    __tablename__ = 'generos'
    id = Column(Integer,primary_key=True)
    descripcion = Column(String(45))

class Favorito(Base):
    __tablename__ = 'favoritos'
    usuarios_id = Column(Integer,ForeignKey=True)
    usuarios = relationship('usuarios',secondary='favorito_usuario',cascade='all,delete,delete-orpha')
    peliculas_id = Column(Integer,ForeignKey=True)
    peliculas = relationship('peliculas',secondary='favorito_pelicula',cascade='all,delete,delete-orpha')


engine = create_engine('mysql+pymysql://root:1BhbbC645h5dAaG6a5-6gBbg1EF1541g@monorail.proxy.rlwy.net:19299/ProyectoPY')

Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(engine)