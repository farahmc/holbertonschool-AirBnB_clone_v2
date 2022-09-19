#!/usr/bin/python3
""" script that starts a Flask web application.
Your web application must be listening on 0.0.0.0, port 5000 """

from flask import Flask, render_template
from models import storage
from models import State

app = Flask(__name__)


@app.teardown_appcontext
def shutdown_session(exception=None):
    """ remove the current SQLAlchemy session """
    storage.close()


@app.route("/states", strict_slashes=False)
@app.route("/states/<id>", strict_slashes=False)
def states_id(id=None):
    """ displays all states or cities by state id"""
    state_dict = storage.all(State).values()
    match = None
    for state in state_dict:
        if id == state.id:
            match = state
    return render_template("9-states.html", state_dict=state_dict, id=id,
                           state=match)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
