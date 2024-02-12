from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os

login_manager = LoginManager()
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.urandom(24)
    app.config.from_object('config.Config')
    app.config['UPLOAD_FOLDER'] = './app/static/imagenes/Peliculas'

    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'usuario.login'

    @login_manager.user_loader
    def load_user(user_id):
        # Importa Usuario dentro de la función para evitar la importación circular
        from .models.usuario import Usuario
        return Usuario.query.get(int(user_id))

    from app.routes import usuario_routes, pelicula_routes, genero_routes, rol_routes, favorito_routes
    app.register_blueprint(usuario_routes.bp)
    app.register_blueprint(pelicula_routes.bp)
    app.register_blueprint(genero_routes.bp)
    app.register_blueprint(rol_routes.bp)
    app.register_blueprint(favorito_routes.bp)

    return app
