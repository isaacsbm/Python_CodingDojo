from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World!"

@app.route("/dojo")
def dojo():
    return "Dojo!"

@app.route("/say/<name>")
def say_hello(name):
    return f"Hello {name}!"

@app.route("/<int:num>/<name>")
def test(num,name):
    return str(num * name)

if __name__ == '__main__':
    app.run(debug=True)


