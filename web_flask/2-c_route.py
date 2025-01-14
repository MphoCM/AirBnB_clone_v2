#!/usr/bin/python3
"""This application listens on 0.0.0.0, port 5000.
Routes:
/: display "Hello HBNB!"
/hbnb: display "HBNB"
/c/<text>: display “C ” followed by the value\
    of the text variable\
        (replace underscore _ symbols with a space )
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def home():
    """Displays 'Hello HBNB!'"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hello_hbnb():
    """/hbnb route : display HBNB"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def dynamic_route(text):
    """Displays 'C' followed by the value of <text>."""
    text = text.replace("_", " ")
    return f"C {text}"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
