from flask import render_template
from flask_app import app

@app.route("/")
def index():
    return render_template("add_author.html")

# author's page that lists all authors and has a function to create a new author

@app.route("/authors")
def create_authors():
    pass
# Book's page that lists all books and has an option to create a new book
@app.route("/books")
def create_books():
    pass
# Author's page that has their favorite's and a function to add their favorite
@app.route("/authors/<int:id>")
def authors_favorites(id):
    pass

#Book's page that has the favorited people and an option to add an author to favorite it.
@app.route("/books/<int:id>")
def books_and_authors(id):
    pass