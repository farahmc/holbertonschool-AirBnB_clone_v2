#!/usr/bin/python3
""" script that starts a Flask web application.
Your web application must be listening on 0.0.0.0, port 5000 """

from flask import Flask
from models import storage
from models import State
from flask import render_template

app = Flask(__name__)


@app.teardown_appcontext
def shutdown_session(exception=None):
    """ remove the current SQLAlchemy session """
    storage.close()


@app.route("/states_list", strict_slashes=False)
def states_list():
    """ display list of states """
    return render_template("7-states_list.html", state_dict=storage.all(State))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
