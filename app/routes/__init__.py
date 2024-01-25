from flask import Blueprint

bp = Blueprint('main', __name__)

from app.routes import usuario_routes, pelicula_routes,genero_routes,favorito_routes,rol_routes
