from flask import Blueprint,render_template,request,redirect,url_for
from app.models.genero import Genero

from app import db 

bp = Blueprint('genero',__name__)

@bp.route('/Genero')
def index():
    data = Genero.query.all()
    return render_template('generos/index.html',data = data)

@bp.route('/Genero/add', methods=['GET','POST'])
def add():
    if request.method == 'POST':
        descripcion = request.form['descripcionGenero']
        
        new_Genero = Genero(descripcion= descripcion)
        db.session.add(new_Genero)
        db.session.commit()
        
        return redirect(url_for('genero.index'))
    data = Genero.query.all()
    return render_template('generos/add.html',data = data)

@bp.route('/Genero/edit/<int:id>', methods=['GET','POST'])
def edit(id):
    genero= Genero.query.get_or_404(id)
    
    if request.method == 'POST':
        genero.descripcion = request.form['descripcionGenero']
        
        db.session.commit()
        
        return redirect(url_for('genero.index'))

    return render_template('generos/add.html', genero=genero )

@bp.route('/Genero/delete/Genero/<int:id>', methods=['GET','POST'])
def delete(id):
    genero= Genero.query.get_or_404(id)
    
    db.session.delete(genero)
    db.session.commit()
        
    return redirect(url_for('genero.index'))

