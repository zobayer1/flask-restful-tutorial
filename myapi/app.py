# -*- coding: utf-8 -*-
import os

from flask import Flask
from flask_cors import CORS
from logging_.config import YAMLConfig

from myapi.commons.errors import register_error_handlers
from myapi.endpoints.v1.books import books_blueprint
from myapi.endpoints.v1.health import health_blueprint
from myapi.extensions import db


def create_app(instance_name: str, app_name: str = "myapi"):
    """Creates a Flask app"""
    instance_path = os.path.join(os.getcwd(), "instance")
    initialize_logging(f"{instance_name}/logging.yaml", instance_path, silent=True)
    app = Flask(
        app_name,
        instance_path=instance_path,
        static_url_path="/myapi/static",
        static_folder="myapi/static",
        instance_relative_config=True,
    )
    app.config.from_object("myapi.config")
    app.config.from_pyfile(f"{instance_name}/application.cfg", silent=True)
    initialize_extensions(app)
    initialize_blueprints(app)
    register_error_handlers(app)
    return app


def initialize_logging(filename: str, instance_path: str, **kwargs: bool):
    """Initializes logging, must be done before creating Flask app"""
    YAMLConfig.from_file(os.path.join(instance_path, filename), **kwargs)


def initialize_extensions(app: Flask):
    """Initializes extensions with app config"""
    CORS(app)
    db.init_app(app)


def initialize_blueprints(app: Flask):
    """Initializes blueprints with URL prefixes"""
    app.register_blueprint(health_blueprint, url_prefix="/myapi/v1/health")
    app.register_blueprint(books_blueprint, url_prefix="/myapi/v1/books")
