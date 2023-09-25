#!/usr/bin/python3
"""
Starts the flask web application
listens to 0.0.0.0:5000
Routes:
    /hbnb_filters: HBNB HTML filters page.
"""

from models import storage
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    """
    Displays the main HBNB filters HTML page.
    """
    states = storage.all("State")
    amenities = storage.all("Amenity")
    return render_template(
            "10-hbnb_filters.html", states=states, amenities=amenities
            )


@app.teardown_appcontext
def teardown(exc):
    """Remove the current SQLAlchemy session."""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
