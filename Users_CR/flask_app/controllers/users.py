from flask import render_template,request, redirect, url_for
from flask_app import app
from flask_app.models.user import User

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/read_all")
def read_all():
    user_list = User.get_all()
    print(user_list)
    return render_template("readall.html", users=user_list)

@app.route("/process", methods=["POST"])
def process():
    if "id" in request.form:
        data = {
            "id":request.form["id"],
            "fn": request.form["first_name"],
            "ln": request.form["last_name"],
            "email": request.form["email"]
            # "ca":request.form["created_at"]
        }
        User.update_user(data)
        return redirect(url_for("read_all"))
    else:
        data = {
            "fn": request.form["first_name"],
            "ln": request.form["last_name"],
            "email": request.form["email"]
        }
        User.create_user(data)
    # if request.form["which_form"] == "create":
    #     id = User.create_user(data)
        return redirect(url_for("index"))

@app.route("/read_one/<int:id>")
def read_one(id):
    data = {
        "id":id
    }
    return render_template("readone.html",user=User.get_one(data))

@app.route("/edit/<int:id>", methods=["GET","POST"])
def edit(id):
    
    return render_template("edit.html", id=id)
    # return redirect(url_for("edit.html"))

@app.route("/delete/<int:id>")
def delete(id):
    User.delete_user({"id": id})
    return redirect(url_for("read_all"))

@app.route("/create", methods=["POST"])
def creation():
    data = {
        "fn": request.form.get("first_name"),
        "ln": request.form.get("last_name"),
        "email": request.form.get("email")
    }
    User.create_user(data)
    return redirect(url_for("read_all"))

@app.route("/update/<int:id>", methods=["POST"])
def updating(id):
    data = {
        "id": id,
        "fn": request.form.get("first_name"),
        "ln": request.form.get("last_name"),
        "email": request.form.get("email")
    }
    User.update_user(data)
    return redirect(url_for("read_all"))

