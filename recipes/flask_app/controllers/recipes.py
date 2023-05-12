from flask import render_template,request, redirect, url_for, session
from flask_app import app
from flask_app.models import recipe
from flask_app.models import user

@app.route("/recipes")
def show_all_recipes():
    if "user_id" not in session:
        return redirect("/login_form")
# @app.route("/recipes")
# def show_all_recipes():
#     user_id = session.get("logged_in")
#     if user_id:
#         data = {
#             'id': id,
#             # 'first_name': first_name
#         }
#         recipes = recipe.Recipe.get_all_recipes()
#         return render_template("dashboard.html", recipes = recipes, )
#     else:
#         return "You are not logged in!"

@app.route("/view_recipe/<int:id>")
def read_one_recipe(id):
    user_id = session.get("logged_in")
    if user_id:
        data = {
            'id': id
            # 'first_name': reqfirst_name
        }
        recipes = recipe.Recipe.get_one_recipe(data)
        return render_template("view_recipe.html", recipe=recipes)

@app.route("/recipe/new")
def render_recipe_new():
    return render_template("create_recipe.html")

@app.route("/create_recipe", methods=["POST"])
def create_recipe():
    data = {
    "name": request.form.get("name"),
    "des": request.form.get("description"),
    "inst": request.form.get("instruction"),
    "u3":request.form.get("under_30_min"),
    "ct": request.form.get("created_at")
}
    recipe.Recipe.create_recipe(data)
    return redirect("/recipes")