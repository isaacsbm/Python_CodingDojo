from flask import render_template, request, redirect, url_for
from flask_app import Flask
from flask_app.models.ninja import Ninja

@app.route("/create_ninja")
def create_ninja():
    data = {
        "fn": request.form.get("first_name"),
        "ln": request.form.get("last_name"),
        "email": request.form.get("email")
    }
    Ninja.create_ninja(data)
    return redirect(url_for("/ninjas/dojos"))
