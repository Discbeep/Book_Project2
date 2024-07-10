from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_URL = "https://api.example.com/books"  # Replace with the actual API URL

@app.route('/')
def index():
    response = requests.get(API_URL)
    books = response.json()[:10]
    return render_template('index.html', books=books)

@app.route('/book/<int:book_id>')
def book_details(book_id):
    response = requests.get(f"{API_URL}/{book_id}")
    book = response.json()
    return render_template('book_details.html', book=book)

if __name__ == '__main__':
    app.run(debug=True)
