#!/usr/bin/python3
"""
Starts the Flask Web App
The appicatopm listens through 0.0.0.0:5000
Routes: 
    /cities_by_states: HTML page with a list of all states and related cities.
"""

from flask import Flask
from models import storage
from flask import render_template

app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    """
    Displays an HTML page with a list of all states and related cities
    States/citis are sorted by their name
    """
    states = storage.all("State")
    return render_template("8-cities_by_states.html", states=states)

@app.teardown_appcontext
def teardown(exc):
    """
    Remove the current SQLAlchemy session.
    """
    storage.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0")
