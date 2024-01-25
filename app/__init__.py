from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    
    db.init_app(app)

    from app.routes import usuario_routes, pelicula_routes,genero_routes,rol_routes,favorito_routes
    app.register_blueprint(usuario_routes.bp)
    app.register_blueprint(pelicula_routes.bp)
    app.register_blueprint(genero_routes.bp)
    app.register_blueprint(rol_routes.bp)
    app.register_blueprint(favorito_routes.bp)

    return app