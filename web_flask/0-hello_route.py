#!/usr/bin/python3
"""
Starts a Falsk web application
"""

from flask import Flask

app = Flask(__name__)

""" Defines the route fot the routing url"""


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Displays the message 'Hello HBNB! """
    return "Hello HBNB!"


if __name__ == "__main__":
    """
    Start the Flask development server
    listens on all available nat (0.0.0.0) port 5000
    """
    app.run(host='0.0.0.0', port=5000)
