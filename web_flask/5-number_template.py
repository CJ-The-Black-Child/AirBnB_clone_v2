#!/usr/bin/python3
"""
Starts the Flask web application
Routes:
    /- display "Hello HBNB!"
    /c/<text> - display "C <text"
    /python/<text> - displays "Python is cool"
    /number/<n> - display n if integer
    /number_template/<n> - display a HTML page if n is an integer
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hbnb_route():
    """
    This prints Hello HBNB
    """
    return "Hello HBNB"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Prints hbnb
    """
    return "HBNB"

@app.route('/c/<string:text>', strict_slashes=False)
def c_text(text):
    """
    Prints C <text content>
    """
    return "C %s" % text

@app.route('/python', strict_slashes=False)
@app.route('python/<string:text>', strict_slashes=False)
def python_text(text="is cool"):
    """
    Prints python is cool
    """
    text = text.replace("_", " ")
    return "Python %s" % text

@app.route('/number/<int:n>', strict_slashes=False)
def number_n(n):
    """
    Displays n if its an integer
    """
    return "%i is a number" % n

@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """
    Displays a HTML page if n is int
    """
    return render_template('5-number.html', n=n)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
