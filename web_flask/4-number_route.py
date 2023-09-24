#!/usr/bin/python3
"""
Starts the flask aeb application
Routes:
    / - display "Hello HBNB!"
    /c/<text> - displays "C <text>"
    /hbnb - displays "HBNB"
    /python/<text> - displays "Python is cool"
    /number/<n> - display n incase there is an integer
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_route():
    """
    Prints the text "Hello HBNB"
    """
    return ("Hello HBNB!")


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    prints HBNB
    """
    return ("HBNB")


@app.route('/c/<string:text>', strict_slashes=False)
def c_text(text):
    """
    Prints C <text> content
    """
    text = text.replace("_", " ")
    return ("C %s" % text)


@app.route('/python', strict_slashes=False)
@app.route('/python/<string:text>', strict_slashes=False)
def python_text(text="is cool"):
    """
    This prints python is cool
    """
    text = text.replace("_", " ")
    return ("Python %s" % text)


@app.route('/number/<int:n>', strict_slashes=False)
def number_n(n):
    """
    Displays n if there is an integer
    """
    return "%i is a number" % n


if __name__ == "__main__":
    app.run("host=0.0.0.0")
