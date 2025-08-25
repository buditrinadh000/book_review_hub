from flask import Flask, render_template, request, redirect, url_for
import uuid

app = Flask(__name__)
books = []

@app.route('/')
def home():
    return render_template('home.html', books=books)

@app.route('/add', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        new_book = {
            'id': str(uuid.uuid4()),
            'title': request.form['title'],
            'author': request.form['author'],
            'description': request.form['description'],
            'reviews': []
        }
        books.append(new_book)
        return redirect(url_for('home'))
    return render_template('add_book.html')

@app.route('/book/<id>')
def book_detail(id):
    book = next((b for b in books if b['id'] == id), None)
    if not book:
        return "Book not found", 404
    return render_template('book_detail.html', book=book)

@app.route('/review/<id>', methods=['GET', 'POST'])
def add_review(id):
    book = next((b for b in books if b['id'] == id), None)
    if not book:
        return "Book not found", 404
    if request.method == 'POST':
        review = {
            'reviewer': request.form['reviewer'],
            'rating': int(request.form['rating']),
            'text': request.form['text']
        }
        book['reviews'].append(review)
        return redirect(url_for('book_detail', id=id))
    return render_template('add_review.html', book=book)

if __name__ == '__main__':
    app.run(debug=True)