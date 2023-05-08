from flask import render_template, request, redirect, url_for
from flask_app import app
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

@app.route("/ninjas/create_ninja", methods=["POST"])
def create_ninja():
    data = {
        "fn": request.form.get("first_name"),
        "ln": request.form.get("last_name"),
        "email": request.form.get("email")
    }
    Ninja.create_ninja(data)
    dojos = Dojo.get_all_dojos()
    return render_template("dojo.html", dojo_list=dojos)

# @app.route("/ninjas/edit/<int:id>", methods=["GET","POST"])
# def edit(id):
#     data = {
#     "id": request.form.get("id"),
#     "fn": request.form.get("first_name"),
#     "ln": request.form.get("last_name"),
#     "age": request.form.get("age")
#     }
#     ninja_id = Ninja.get_one_by_id(id)
#     return render_template("edit.html", ninja=ninja_id)

@app.route("/ninjas/update/<int:id>", methods=["POST", "GET"])
def update(id):
    data = {
        "id": request.form.get("id"),
        "fn": request.form.get("first_name"),
        "ln": request.form.get("last_name"),
        "age": request.form.get("age")
    }
    Ninja.update_user(data)
    return render_template("edit.html", id=id)
