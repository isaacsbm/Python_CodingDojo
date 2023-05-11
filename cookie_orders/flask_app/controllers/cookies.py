from flask import render_template, redirect, url_for, request
from flask_app import app
from flask_app.models import cookies_and_customers

# * Starting Route
@app.route("/")
def index():
    return redirect(url_for("cookies_new"))

# * Redirect for index
@app.route("/cookies/new")
def cookies_new():
    return render_template("cookie_order.html")

# ! Show all for cookie orders
@app.route("/cookies")
def show_orders():
    order_list = cookies_and_customers.Cookies.get_all_cookies()
    print(order_list)
    return render_template("show_orders.html", orders = order_list)

# ! Logs a new order
@app.route("/create_order", methods=["POST", "GET"])
def create_order():
    if not cookies_and_customers.Cookies.is_valid(request.form):
        return redirect(url_for("cookies_new"))
    else:
        data = {
            "name": request.form.get("name"),
            "ct": request.form.get("cookie_type"),
            "nob": request.form.get("num_of_boxes")
        }
        cookies_and_customers.Cookies.create_order(data)
        return redirect("/cookies")

# ! Edit Page Link
@app.route("/edit/<int:id>")
def edit_page(id):
    data = {
        "id":id
    }
    cookies_and_customers.Cookies.get_one_order(data)
    return render_template("edit_order.html", id=id)

# ! Update's existing order
@app.route("/update/<int:id>", methods=["POST"])
def update_order(id):
    if not cookies_and_customers.Cookies.is_valid(request.form):
        print(request.form)
        return redirect(url_for("edit_page", id=id))
    else:
        data = {
        "id": id,
        "name": request.form.get("name"),
        "ct": request.form.get("cookie_type"),
        "nob": request.form.get("num_of_boxes")
        }
        cookies_and_customers.Cookies.edit_order(data)
        return redirect(url_for("show_orders", id=id))