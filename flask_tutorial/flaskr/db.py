import sqlite3

import click
from flask import current_app, g
from flask.cli import with_appcontext


def get_db():
    if 'db' not in g:

        # establishes a connection to the file pointed at by the DATABASE configuration key
        g.db = sqlite3.connect(

            # special object that points to the Flask application handling the request
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )

        # sqlite3.Row tells the connection to return rows that behave like dicts. This allows accessing the columns by name.
        g.db.row_factory = sqlite3.Row

    return g.db

# close_db checks if a connection was created by checking if g.db was set


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()
