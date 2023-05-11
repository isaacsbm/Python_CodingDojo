from flask import render_template,request, redirect, url_for
from flask_app import app
# from flask_app.models.user import User

@app.route("/")
def index():
    return render_template("registration.html")