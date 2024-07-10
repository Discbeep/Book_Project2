from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    response = requests.get('http://openlibrary.org/search.json?q=the')
    books = response.json().get('docs', [])[:10]
    return render_template('index.html', books=books)

@app.route('/book/<book_id>')
def book_detail(book_id):
    response = requests.get(f'http://openlibrary.org/works/{book_id}.json')
    book = response.json()
    return render_template('book_detail.html', book=book)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
