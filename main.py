from flask import Flask
from flask_restx import Api

from app.config import Config
from app.setup_db import db
from app.views.movie import movie_ns


def create_app(config_object):
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)
    return app


def register_extensions(app):
    db.init_app(app)
    api = Api(app)
    api.add_namespace(movie_ns)


app = create_app(Config())


if __name__ == '__main__':
    app.run()
