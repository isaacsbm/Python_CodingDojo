from flask import render_template,request, session
import random
from flask_app import app


@app.route("/", methods=["POST","GET"])
def index():
    if 'num' not in session:
        session['num'] = random.randint(1,100)
        session['guess'] = 0
    message = None
    if request.method == "POST":
        guess = int(request.form['guess'])
        session['guess'] += 1
        if guess < session['num']:
            message = "Too Low!"
        elif guess > session['num']:
            message = "Too High!"
        else:
            message = "You Win!"
            number = session.pop('num')
            message = f"The number was {number}"
    if session['guess'] >= 5:
        message = f"Sorry! You've reached the max amount of guesses! The number I generated was {session['num']}"
        session.pop('num')
        session.pop('guess')
    return render_template("index.html", message=message)