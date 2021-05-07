# -*- coding: utf-8 -*-
import os

import click
from flask.cli import FlaskGroup

from myapi.app import create_app


def create_cli_app():
    return create_app(os.getenv("FLASK_ENV", "development"))


@click.group(cls=FlaskGroup, create_app=create_cli_app)
def cli():
    """Management interface for myapi"""
    pass


if __name__ == "__main__":
    cli()
