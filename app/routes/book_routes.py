from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from app.models.book import Book
from app.models.author import Author
from app import db

bp = Blueprint('book', __name__)

@bp.route('/')
def index():
    data = Book.query.all()
    # books_list = [book.to_dict() for book in data]
    # return jsonify(books_list)
    return render_template('books/index.html', data=data)
    #return data

@bp.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        titulo = request.form['titulo']
        author = request.form['author']
        
        new_book = Book(titulo=titulo, author=author)
        db.session.add(new_book)
        db.session.commit()
        
        return redirect(url_for('book.index'))
    data = Author.query.all()
    return render_template('books/add.html', data=data)

@bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    book = Book.query.get_or_404(id)

    if request.method == 'POST':
        #return "entra al if"
        book.titulo = request.form['titulo']
        book.author = request.form['author']
        
        db.session.commit()
        
        return redirect(url_for('book.index'))

    return render_template('books/edit.html', book=book)

@bp.route('/delete/<int:id>')
def delete(id):
    book = Book.query.get_or_404(id)
    
    db.session.delete(book)
    db.session.commit()

    return redirect(url_for('Book.index'))
