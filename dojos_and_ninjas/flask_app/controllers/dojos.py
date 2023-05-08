from flask import render_template,request, redirect, url_for
from flask_app import app
from flask_app.models.ninja import Ninja
from flask_app.models import dojo

@app.route("/")
def index():
    return redirect("/ninjas")

# @app.route("/ninjas/process")
#     pass

@app.route("/ninjas")
def ninjas():
    dojos = dojo.Dojo.get_all_dojos()
    return render_template("index.html", dojo_list = dojos)

@app.route("/ninjas/dojos")
def dojos():
    return render_template("dojo.html")

@app.route("/ninjas/show_dojo/<int:id>", methods=["POST", "GET"])
def show_dojo(id):
    data = {
        "id": id
    }
    dojos = dojo.Dojo.get_dojo_with_ninjas(data)
    return render_template("dojo_show.html", dojo = dojos, ninjas = dojos.ninjas)

