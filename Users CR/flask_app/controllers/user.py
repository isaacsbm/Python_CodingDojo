from flask import render_template
from flask_app import app

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/read_all")
def read_all():
    return render_template("readall.html")