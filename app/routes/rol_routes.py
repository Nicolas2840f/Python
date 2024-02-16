from flask import Blueprint,render_template,request,redirect,url_for
from flask_login import login_required
from app.models.rol import Rol

from app import db 

bp = Blueprint('rol',__name__)

@bp.route('/Rol')
@login_required
def index():
    data = Rol.query.all()
    return render_template('roles/add.html',data = data)

@bp.route('/Rol/add', methods=['GET','POST'])
@login_required
def add():
    if request.method == 'POST':
        descripcion = request.form['descripcionRol']
        
        new_Rol = Rol(descripcion = descripcion)
        db.session.add(new_Rol)
        db.session.commit()
        
        return redirect(url_for('rol.index'))
    data = Rol.query.all()
    return render_template('roles/add.html',data = data)

@bp.route('/Rol/edit/<int:id>', methods=['GET','POST'])
@login_required
def edit(id):
    rol= Rol.query.get_or_404(id)
    
    if request.method == 'POST':
        rol.descripcion = request.form['descripcionRol']
        
        db.session.commit()
        
        return redirect(url_for('rol.index'))

    return render_template('roles/add.html', Rol=Rol )

@bp.route('/Rol/delete/<int:id>', methods=['GET','POST'])
@login_required
def delete(id):
    rol= Rol.query.get_or_404(id)
    
    db.session.delete(rol)
    db.session.commit()
        
    return redirect(url_for('rol.index'))

