#!/usr/bin/python3
""" Starts The flask web app """
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hbnb_route():
    """
    Prints the Hello HBNB
    """
    return "Hello HBNB!"


@app.route('/c/<string:text>', strict_slashes=False)
def c_text(text):
    """
    Prints C <text> content
    """
    text = text.replace("_", " ")
    return "C %s" % text


@app.route('/python', strict_slashes=False)
@app.route('python/<string:text>', strict_slashes=False)
def python_text(text="is cool"):
    """
    Prints Python is cool
    """
    text = text.replace("_", " ")
    return "Python %s" % text

@app.route('/number/<int:n>', strict_slashes=False)
def number_n(n):
    """displays n if it is an integer"""
    return "%i is a number" % n

@app.route('number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """Displays a HTML page if n is an integer"""
    return render_template('5-number.html', n=n)

@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """
    Display a HTML page if n is int
    """
    return render_template('6-number_odd_or_even.html', n=n)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
