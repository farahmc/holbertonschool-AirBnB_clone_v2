#!/usr/bin/python3
""" script that starts a Flask web application.
Your web application must be listening on 0.0.0.0, port 5000 """

from flask import Flask, render_template
from models import storage, State, Amenity

app = Flask(__name__)


@app.teardown_appcontext
def shutdown_session(exception=None):
    """ remove the current SQLAlchemy session """
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """ static page displaying states and amenities menus"""
    state_dict = storage.all(State).values()
    amen_dict = storage.all(Amenity).values()
    return render_template('10-hbnb_filters.html',
                           state_dict=state_dict, amen_dict=amen_dict)


if __name__ == "__main__":
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
    app.run(host='0.0.0.0', port=5000, debug=True)
