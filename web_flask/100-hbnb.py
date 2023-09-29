#!/usr/bin/python3
"""
Starts a Flask web application.
this app listens through 0.0.0.0:5000"""

from models import storage
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """This displaus HBNB filters page"""
    states = storage.all("State")
    amenities = storage.all("Amenity")
    places = storage.all("Place")
    return render_template("100-hnbn.html",
            states=states, amenities=amenities,
            places=places)


@app.teardown_appcontext()
def teardown(exc):
    """
    Removes the initial SQLAlchemy session
    """
    storage.close()

if __name__ == "__main__":
    app.run("host=0.0.0.0")
