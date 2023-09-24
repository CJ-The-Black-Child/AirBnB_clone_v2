#!/usr/bin/python3
"""
Starts a Falsk web application
"""

from flask import Flask


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Displays 'Hello HBNB!'
    """
    return ("Hello HBNB!")


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Displays 'HBNB'
    """
    return ("HBNB")


if __name__ == "__main__":
    """
    Starts the dev server
    also listens to all available network interfaces (0.0.0.0) and
    port port 5000
    """
    app.run(host='0.0.0.0', port=5000)
