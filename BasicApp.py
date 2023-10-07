from flask import Flask, render_template, request, redirect, url_for
from tinydb import TinyDB, Query

app = Flask(__name__)
db = TinyDB('my_database.json')
table = db.table('papers')
@app.route('/')
def index():
    books = table.all()
    return render_template('index.html', books=books)

@app.route('/add', methods=['POST'])
def add():
    title = request.form.get('title')
    author = request.form.get('author')
    year = request.form.get('year')
    publisher = request.form.get('publisher')

    table.insert({'title': title, 'author': author, 'year': year, 'publisher': publisher})
    return redirect(url_for('index'))

@app.route('/edit/<int:book_id>', methods=['GET', 'POST'])
def edit(book_id):
    book = table.get(doc_id=book_id)

    if request.method == 'POST':
        title = request.form.get('title')
        author = request.form.get('author')
        year = request.form.get('year')
        publisher = request.form.get('publisher')

        table.update({'title': title, 'author': author, 'year': year, 'publisher': publisher}, doc_ids=[book_id])
        return redirect(url_for('index'))
    return render_template('edit.html', book=book)

@app.route('/delete/<int:book_id>')
def delete(book_id):
    table.remove(doc_ids=[book_id])
    return redirect(url_for('index'))

@app.route('/search', methods=['GET'])
def search():
    search_query = request.args.get('search')
    books = table.search(
        (Query().title.search(search_query)) |
        (Query().author.search(search_query)) |
        (Query().year.search(search_query)) |
        (Query().publisher.search(search_query))
    )
    return render_template('search_results.html', books=books)

if __name__ == '__main__':
    app.run(debug=True)
