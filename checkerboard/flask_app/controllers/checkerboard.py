from flask import render_template,request, redirect, url_for
from flask_app import app

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/<int:num_row>/<int:num_col>")
def checkerboard(num_row, num_col):
    return render_template("index.html", num_row=num_row, num_col = num_col )

# @app.route("/<int:num_row>/<int:num_col>/<color1>/<color2>")
# def color_checkerboard(num_row, num_col, color1, color2):
#     return render_template("index.html", num_row=num_row, num_col = num_col, color1 = color1, color2 = color2)
