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
            "email": request.form["email"],
            "ca":request.form["created_at"]
        }
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

@app.route("/edit", methods=["POST"])
def edit():
    User.update_user(request.form)
    return redirect("edit.html")

# @app.route("/users/delete/<int:id>")
# def delete(id):
#     data = {
#         "id":id
#     }
#     User.delete(data)
#     return redirect(url_for("index"))