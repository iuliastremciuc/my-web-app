
# web_app/routes/book_routes.py

from flask import Blueprint, jsonify, render_template, request, redirect

from web_app.models import db, Book, parse_records

book_routes = Blueprint("book_routes", __name__)

@book_routes.route("/books.json")
def list_books():
    print("REQUESTED THE BOOKS IN JSON FORMAT")
    #books = [
    #    {"id": 1, "title": "Book 1"},
    #    {"id": 2, "title": "Book 2"},
    #    {"id": 3, "title": "Book 3"},
    #] # todo: get from the database
    book_records = Book.query.all()
    books = parse_records(book_records)
    return jsonify(books)

@book_routes.route("/books")
def books():
    print("VISITED THE BOOKS PAGE")
    #books = [
    #    {"id": 1, "title": "Book 1"},
    #    {"id": 2, "title": "Book 2"},
    #    {"id": 3, "title": "Book 3"},
    #] # todo: get from the database
    book_records = Book.query.all()
    return render_template("books.html", books=book_records)

@book_routes.route("/books/new")
def new_book():
    return render_template("new_book.html")

@book_routes.route("/books/create", methods=["POST"])
def create_book():
    print("FORM DATA:", dict(request.form))
    # todo: store in database
    #return jsonify({
    #    "message": "BOOK CREATED OK (TODO)",
    #    "book": dict(request.form)
    #})
    new_book = Book(title=request.form["book_title"], author_id=request.form["author_name"])
    print(new_book)
    db.session.add(new_book)
    db.session.commit()
    #flash(f"Book '{new_book.title}' created successfully!", "success")
    return redirect("/books")