from app import create_app,db
import os

app = create_app()
app.config['SECRET_KEY'] = os.environ.get('FLASK_SECRET_KEY', 'una_clave_secreta_por_defecto')

with app.app_context():
    db.create_all()

if __name__ == '__main__':
     app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))