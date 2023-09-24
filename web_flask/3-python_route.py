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
    text_formatted = text.replace("_", " ")
    return "C {}".format(text_formatted)

@app.route('/python', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('python/<text>', strict_slashes=False)
def python_text(text):
    """
    Prints the text Python is cool
    """
    text_formatted = text.replace("_", " ")
    return "Python {}".format(text_formatted)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
