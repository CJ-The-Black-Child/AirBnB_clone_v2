#!/usr/bin/python3
"""
Starts the flask web application
"""

from flask import Flask
from models import storage
from flask import render_template

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list():
    """
    Displays an HTML page with a list of all state objects in a DB storage
    note that states are sorted
    """
    states = storage.all("State")
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def teardown(exc):
    """
    Remove the current SQLAlchemy session
    """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
