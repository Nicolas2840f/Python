from flask import Blueprint,render_template,request,redirect,url_for,Flask,flash,session
from flask_bcrypt import Bcrypt
from app.models.usuario import Usuario

from app import db 

bp = Blueprint('usuario',__name__)
app = Flask(__name__)

bcrypt = Bcrypt(app) 

@bp.route('/')
def index():
    return render_template('usuarios/index.html')

@bp.route('/add', methods=['GET','POST'])
def add():
    if request.method == 'POST':
        nombre = request.form['nombreUsuario']
        telefono = request.form['telefonoUsuario']
        email = request.form['emailUsuario']
        password = request.form['passwordUsuario']
        passwordConfirmation = request.form['passwordConfirmation']
        rol = 1
        if password == passwordConfirmation:
            hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
            new_Usuario = Usuario(nombre = nombre,telefono = telefono,email = email,password = hashed_password,rol = rol)
            db.session.add(new_Usuario)
            db.session.commit()
            return redirect(url_for('.index'))
        
    
    return render_template('usuarios/add.html')

@bp.route('/edit/<int:id>', methods=['GET','POST'])
def edit(id):
    usuario= Usuario.query.get_or_404(id)
    
    if request.method == 'POST':
        usuario.nombre = request.form['nombreUsuario']
        usuario.telefono = request.form['telefonoUsuario']
        usuario.email = request.form['emailUsuario']
        usuario.password = request.form['passwordUsuario']
        
        db.session.commit()
        
        return redirect(url_for('usuario.index'))

    return render_template('usuarios/add.html', usuario=usuario )

@bp.route('/delete/<int:id>', methods=['GET','POST'])
def delete(id):
    usuario= Usuario.query.get_or_404(id)
    
    db.session.delete(usuario)
    db.session.commit()
        
    return redirect(url_for('usuario.index'))

@bp.route('/auth', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form['emailUsuario']
        password = request.form['passwordUsuario']

        # Verifica que todos los campos estén llenos
        if not email or not password:
            flash('Todos los campos son obligatorios', 'error')
            return render_template('usuarios/index.html')

        user = Usuario.query.filter_by(email=email).first()

        if user:
            # El usuario ya existe, intenta iniciar sesión
            if bcrypt.check_password_hash(user.password, password):
                # Autenticación exitosa, inicia sesión
                # session['user_id'] = user.id  # Puedes almacenar más información del usuario en la sesión si es necesario
                # session['user_name'] = user.nombre 
                # session['user_phone'] = user.telefono  
                flash('Inicio de sesión exitoso', 'success')
                return redirect(url_for('pelicula.index'))
            else:
                flash('Usuario o contraseña incorrectos', 'error')

    return render_template('usuarios/index.html')