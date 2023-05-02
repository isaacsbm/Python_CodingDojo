from flask import Flask

app=Flask(__name__)
app.secret_key="hello_there"

if __name__ == "__main__":
    app.run(debug=True)