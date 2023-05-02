from flask import Flask, render_template, request, session
app= Flask(__name__)
app.secret_key="hello_there"

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == "POST":
        session['name']= request.form['name']
        session['location'] = request.form['location']
        session['favorite_language'] = request.form['favorite_language']
        session['comment'] = request.form['comment']
    return render_template("index.html")


@app.route('/result')
def result():
    name = session.get('name')
    location = session.get('location')
    favorite_language = session.get('favorite_language')
    comment = session.get('comment')
    return render_template("result.html", name=name, location=location, favorite_language=favorite_language, comment=comment)

if __name__=='__main__':
    app.run(debug=True, port=4999)