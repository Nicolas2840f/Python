from flask import Blueprint,render_template,request,redirect,url_for,Flask,flash,session
from flask_bcrypt import Bcrypt
from flask_login import login_user, logout_user, login_required,current_user
from app.models.usuario import Usuario
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
from app import db
import secrets
import smtplib
import os
 

bp = Blueprint('usuario',__name__)
app = Flask(__name__)

bcrypt = Bcrypt(app) 

@bp.route('/',methods=['GET','POST'])
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
                login_user(user)
                # Autenticación exitosa, inicia sesión
                session['idUsuario'] = user.id  # Puedes almacenar más información del usuario en la sesión si es necesario
                session['nombreUsuario'] = user.nombre 
                session['telefonoUsuario'] = user.telefono  
                session['rolUsuario'] = user.rol  

                flash('Inicio de sesión exitoso', 'success')
                return redirect(url_for('pelicula.index'))
            else:
                flash('Usuario o contraseña incorrectos', 'error')
    if current_user.is_authenticated:
        return redirect(url_for('pelicula.index'))
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
            return redirect(url_for('usuario.login'))
        
    
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
        
        return redirect(url_for('usuario.login'))

    return render_template('usuarios/add.html', usuario=usuario )

@bp.route('/delete/<int:id>', methods=['GET','POST'])
def delete(id):
    usuario= Usuario.query.get_or_404(id)
    
    db.session.delete(usuario)
    db.session.commit()
        
    return redirect(url_for('usuario.login'))

@bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('usuario.login'))

@bp.route('/reset', methods=['GET', 'POST'])
def reset():
    if request.method == 'POST':
        email = request.form['emailUsuario']

        if not email:
            flash('Todos los campos son obligatorios', 'error')
            return render_template('usuarios/reset.html')

        user = Usuario.query.filter_by(email=email).first()
        if user:
            reset_code = secrets.token_hex(3)
            session['reset_code'] = reset_code
            try:
                load_dotenv()
                servidor_smtp = smtplib.SMTP(os.getenv("smtp_host"), os.getenv("smtp_port"))
                servidor_smtp.starttls()
                servidor_smtp.login(os.getenv("smtp_user"), os.getenv("smtp_password"))

                msg = MIMEMultipart()
                msg["From"] = os.getenv('smtp_user')
                msg["To"] = 'ncastaneda840@misena.edu.co'
                msg["Subject"] = "Sugerencias"
                msg.attach(MIMEText('Hola'))

                servidor_smtp.sendmail( os.getenv("smtp_user"),'ncastaneda840@misena.edu.co', msg.as_string())
                servidor_smtp.quit()

                return render_template('usuarios/code.html')
            except Exception as e:
                return str(e)

        else:
            flash('El email no está registrado en la base de datos', 'error')
            return render_template('usuarios/reset.html')
    return render_template('usuarios/reset.html')