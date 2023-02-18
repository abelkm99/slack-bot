# create the flask app here
from flask import Flask, request
from app.extensions import bcrypt, db, cors, jwt, migrate
from app.api import api_blueprint
flask_app = Flask(__name__)


def create_app(config_object):
    app = Flask(__name__)
    app.url_map.strict_slashes = False
    app.config.from_object(config_object)
    app = register_extensions(app)
    app = register_blueprint(app)
    return app


def register_extensions(app):
    bcrypt.init_app(app)
    db.init_app(app)
    # disable caching
    # cache.init_app(app)
    cors.init_app(app,resources={r"*": {"origins": "*"}},supports_credentials=True)
    jwt.init_app(app)
    migrate.init_app(app,db)
    return app

def register_blueprint(app):

    app.register_blueprint(api_blueprint)
    return app