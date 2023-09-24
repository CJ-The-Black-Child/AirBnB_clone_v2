#!/usr/bin/python3
"""
Starts the flask web app
Routes as :
    / - display "Hello HBNB!"
    /hbnb - display "HBNB"
    /c/<text> - display "C <text>"
    /python/<text> - display "Python is cool"
"""

from flask import Flask

app = Flask(__name__)


@app.route('/',strict_slashes=False)
def hello_hbnb():
    """
    Prints the text Hello HBNB
    """
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Prints the text HBNB
    """
    return "HBNB"

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
    Prints the text Python is cool
    """
    text = text.replace("_", " ")
    return "Python %s" % text

if __name__ == "__main__":
    app.run(host="0.0.0.0")
