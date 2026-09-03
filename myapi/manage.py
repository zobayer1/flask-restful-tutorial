# -*- coding: utf-8 -*-
import os

import click
from flask.cli import FlaskGroup

from myapi.app import create_app
from myapi.extensions import db


def create_cli_app():
    return create_app(os.getenv("FLASK_ENV", "development"))


@click.group(cls=FlaskGroup, create_app=create_cli_app)
def cli():
    """Management interface for myapi"""
    pass


@cli.command()
def env():
    """Check env variables for the app."""
    env_vars = ["FLASK_ENV", "FLASK_SECRET", "LOGGING_ROOT", "DATABASE_URI"]
    for var in env_vars:
        click.echo(f"${var}={os.getenv(var)}")


@cli.command()
def init_db():
    """Create the database tables."""
    db.create_all()
    click.echo("Database tables created.")


if __name__ == "__main__":
    cli()
