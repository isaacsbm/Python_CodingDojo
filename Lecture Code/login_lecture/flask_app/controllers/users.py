from flask_app import app
from flask import render_template, request, redirect, url_for, flash, session
from flask_app.models.user import User
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register", methods=["POST"])
def register():
    if not User.is_valid(request.form):
        return redirect(url_for("index"))
    else:
        data = {
            "first_name": request.form["first_name"],
            "last_name": request.form["last_name"],
            "email": request.form["email"],
            "password": bcrypt.generate_password_hash(request.form["password"])
        }
        User.create(data)
        return redirect(url_for("index"))

@app.route("/login_form")
def login_form():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login():
    data = {
        "email" : request.form["email"]
    }
    user_from_db = User.get_by_email(data)

    if not user_from_db:
        flash("Invalid login")
        return redirect(url_for("login_form"))
    if not bcrypt.check_password_hash(user_from_db.password, request.form["password"]):
        flash("Invalid login")
        return redirect(url_for("login_form"))
    
    session["logged_in"] = user_from_db.id
    return redirect(url_for("dashboard"))

@app.route("/success")
def dashboard():
    logged_in = User.get_by_id({"id":int(session["logged_in"])})
    print(logged_in)
    return logged_in.full_name()
