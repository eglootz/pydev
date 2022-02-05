import os
from flask import Flask

# create flask instance


def create_app(test_config=None):
    # __name__ is the location where everything has to be set up
    # instance_relative_config=True tells the program that the files are relative to the instance folder (holds local data such as as configuration or databases)
    app = Flask(__name__, instance_relative_config=True)

    # sets default configuration
    # secret key will be overwritten, shows the database path
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        # overrides default configuration and values (e.g. the secret key) found in the config.py file
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance (app.instance_path) folder exists and creates it if not
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    # creates connection between /hello and the page saying Hello, World!
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    return app
