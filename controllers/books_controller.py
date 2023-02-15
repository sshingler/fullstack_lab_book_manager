from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.book import Book
from repositories import author_repository, book_repository

books_blueprint = Blueprint("books", __name__)

@books_blueprint.route("/books")
def books():
    books = book_repository.select_all()
    return render_template("books/index.html", all_books = books)

