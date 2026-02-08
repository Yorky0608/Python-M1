from flask import Flask, request, jsonify, abort, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(200), nullable=False)
    author = db.Column(db.String(200), nullable=False)
    publisher = db.Column(db.String(200), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'book_name': self.book_name,
            'author': self.author,
            'publisher': self.publisher,
        }


def create_tables():
    db.create_all()


@app.route('/books', methods=['GET'])
def list_books():
    books = Book.query.all()
    return jsonify([b.to_dict() for b in books])


@app.route('/books', methods=['POST'])
def create_book():
    data = request.get_json() or {}
    for field in ('book_name', 'author', 'publisher'):
        if field not in data:
            return jsonify({'error': f"Missing field: {field}"}), 400

    book = Book(book_name=data['book_name'], author=data['author'], publisher=data['publisher'])
    db.session.add(book)
    db.session.commit()
    return jsonify(book.to_dict()), 201, {'Location': url_for('get_book', book_id=book.id)}


@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = Book.query.get_or_404(book_id)
    return jsonify(book.to_dict())


@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    book = Book.query.get_or_404(book_id)
    data = request.get_json() or {}
    for field in ('book_name', 'author', 'publisher'):
        if field not in data:
            return jsonify({'error': f"Missing field: {field}"}), 400

    book.book_name = data['book_name']
    book.author = data['author']
    book.publisher = data['publisher']
    db.session.commit()
    return jsonify(book.to_dict())


@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    book = Book.query.get_or_404(book_id)
    db.session.delete(book)
    db.session.commit()
    return '', 204


if __name__ == '__main__':
    with app.app_context():
        create_tables()
    app.run(debug=True)
