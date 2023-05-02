from flask import Flask, render_template, session

app = Flask(__name__)
app.secret_key = "hello_there"

@app.route('/')
def index():
    session['count'] = session.get('count', 0)+1
    return render_template("index.html", count=session['count'])

@app.route('/destroy_session')
def destroy_session():
    session.pop('count', None)
    return render_template("index.html")

@app.route('/plus_two')
def plus_two():
    session['count'] = session.get('count', 0) + 2
    return render_template("index.html", count=session['count'])


if __name__ == '__main__':
    app.run(debug=True, port=4999)