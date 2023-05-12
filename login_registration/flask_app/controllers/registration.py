from flask_app import app
from flask import render_template, request, redirect, url_for, flash, session
from flask_bcrypt import Bcrypt
from flask_app.models import user
bcrypt = Bcrypt(app)

@app.route("/")
def index():
    return render_template("index.html") 

@app.route("/register", methods=["POST"])
def register():
    print(request.form)
    if not user.User.is_valid(request.form):
        return redirect(url_for("index"))
    else:
        data = {
            "first_name": request.form["first_name"],
            "last_name": request.form["last_name"],
            "email": request.form["email"],
            "password": bcrypt.generate_password_hash(request.form["password"])
        }
        user.User.create(data)
        return redirect(url_for("login_form"))
    
@app.route("/login_form")
def login_form():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login():
    data = {
        "email": request.form["email"]
    }
    user_from_db = user.User.get_by_email(data)
    print(user_from_db)
    
    if not user_from_db:
        flash("Invalid login")
        return redirect(url_for("login_form"))
    if not bcrypt.check_password_hash(user_from_db.password, request.form["pwd"]):
        flash("Invalid login")
        return redirect(url_for("login_form"))
    
    session["logged_in"] = user_from_db.id
    return redirect(url_for("dashboard"))

# * Forgot to add a logout route, added!
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login_form")

# * Updated render_template to go to page!
@app.route("/success")
<<<<<<< HEAD
def dashboard():
    logged_in = user.User.get_by_id({"id": int(session["logged_in"])})
    print(logged_in)
    return render_template("dashboard.html", user=user)
=======
def logged_in():
    user_id = int(session.get("logged_in"))
    if user_id:
        logged_in_user = user.User.get_by_id(user_id)
        return redirect("/dashboard", logged_in_user=logged_in_user)
    else:
        return redirect("/login")
>>>>>>> 6e0f9c4c45ef8f740ad0835ec3968f4a795ef23d
