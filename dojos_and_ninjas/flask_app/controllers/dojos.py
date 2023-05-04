from flask import render_template,request, redirect, url_for
from flask_app import app

@app.route("/")
def index():
    return redirect("/ninjas")

@app.route("/ninjas")
def ninjas():
    return render_template("index.html")

@app.route("/ninjas/dojos")
def dojos():
    return render_template("dojo.html")

@app.route("/ninjas/show_dojo")
def show_dojo():
    return render_template("dojo_show.html")