#!/usr/bin/python3
"""
Starts the flask web applcation.
The app listens through 0.0.0.0:5000.
Routes:
    /states: HTML page with a list of all state objects
    /states/<id>: HTML page displaying the given state with <d>.
"""

from models import storage
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def states():
    """
    Displays an HTML page with a list of all states.
    States are sorted by name.
    """
    states = storage.all("State")
    return render_template("9-states.html", state=states)


@app.route("/states/<id>", strict_slashes=False)
def states_id(id):
    """
    Displays an HTML page with info about <id> if it exists.
    """
    for state in storage.all("State").values():
        if state.id == id:
            return render_template("9-states.html", state=state)
    return render_template("9-states.html")


@app.teardown_appcontext
def teardown(exc):
    """
    Removes the current SQLAlchemy sessionself.
    """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
