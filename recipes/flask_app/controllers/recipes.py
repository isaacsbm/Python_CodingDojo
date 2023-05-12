from flask import render_template,request, redirect, url_for, session, flash
from flask_app import app
from flask_app.models import recipe
from flask_app.models import user

@app.route("/recipes")
def show_all_recipes():
    if "logged_in" not in session:
        flash("Login in!")
        return redirect(url_for("index"))
    users = user.User.get_by_id({"id": int(session["logged_in"])})
    recipes = recipe.Recipe.get_all_recipes()
    return render_template("dashboard.html", users=users, all_recipes=recipes)

@app.route("/view_recipe/<int:id>")
def read_one_recipe(id):
    if "logged_in" not in session:
        flash("Login in!")
        return redirect(url_for("index"))
    users = user.User.get_by_id({"id": int(session["logged_in"])})
    data = {
        'id': id
    }
    recipes = recipe.Recipe.get_one_recipe(data)
    return render_template("view_recipe.html", recipe=recipes, users=users)

@app.route("/recipe/new")
def render_recipe_new():
    if "logged_in" not in session:
        flash("Login in!")
        return redirect(url_for("index"))
    return render_template("create_recipe.html")

@app.route("/create_recipe", methods=["POST"])
def create_recipe():
    if not recipe.Recipe.is_valid(request.form):
        return redirect("/recipe/new")
    else:
        data = {
        "name": request.form.get("name"),
        "des": request.form.get("description"),
        "inst": request.form.get("instruction"),
        "u3":request.form.get("under_30_min"),
        "ct": request.form.get("created_at"),
        "users_id": session["logged_in"]
    }
        recipe.Recipe.create_recipe(data)
        return redirect("/recipes")

@app.route("/recipes/edit/<int:id>")
def edit_recipe(id):
    if "logged_in" not in session:
        flash("Login in!")
        return redirect(url_for("index"))
    data ={
        "id": id
    }
    recipes = recipe.Recipe.get_one_recipe(data)
    return render_template("edit.html", recipes=recipes)

@app.route("/update_recipe/<int:id>", methods=["POST"])
def update_recipe(id):
    if not recipe.Recipe.is_valid(request.form):
        return redirect(url_for("edit_recipe", id=id))
    else:
        data = {
            "id": id,
            "name": request.form.get("name"),
            "des": request.form.get("description"),
            "inst": request.form.get("instruction"),
            "u3":request.form.get("under_30_min"),
            "ua": request.form.get("updated_at"),
            "users_id": session["logged_in"] # This is my hidden data
        }
        recipe.Recipe.update_recipe(data)
        return redirect("/recipes")

@app.route("/delete/<int:id>")
def delete_recipe_forever(id):
    data ={
        "id": id
    }
    recipe.Recipe.delete_recipe(data)
    return redirect("/recipes")