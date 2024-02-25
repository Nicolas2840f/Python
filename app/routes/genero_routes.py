from flask import Blueprint,render_template,request,redirect,url_for,flash
from flask_login import login_required
from app.models.genero import Genero

from app import db 

bp = Blueprint('genero',__name__)

@bp.route('/Genero')
@login_required
def index():
    data = Genero.query.all()
    return render_template('generos/add.html',data = data)

@bp.route('/Genero/add', methods=['GET','POST'])
@login_required
def add():
    if request.method == 'POST':
        descripcion = request.form['descripcionGenero']
        
        new_Genero = Genero(descripcion= descripcion)
        db.session.add(new_Genero)
        db.session.commit()
        flash('Genero agregado con éxito','success')  
        return redirect(url_for('genero.index'))
    data = Genero.query.all()
    return render_template('generos/add.html',data = data)

@bp.route('/Genero/edit/<int:id>', methods=['GET','POST'])
@login_required
def edit(id):
    genero= Genero.query.get_or_404(id)
    
    genero.descripcion = request.form['descripcion']
    db.session.commit()
    flash('Genero modificado con éxito','success')  
    return redirect(url_for('genero.index'))

@bp.route('/Genero/delete/Genero/<int:id>', methods=['GET','POST'])
@login_required
def delete(id):
    genero= Genero.query.get_or_404(id)
    
    db.session.delete(genero)
    db.session.commit()
    flash('Genero eliminado con éxito','success')    
    return redirect(url_for('genero.index'))

