# -*- coding: utf-8 -*-
import os

"""ENV: Flask application environment.

Examples: `development`, `production`, `testing`.
"""
ENV = os.getenv("FLASK_ENV", "development")

"""SECRET_KEY: Secret key used for signing cookies and tokens.

Application will fail to start if $FLASK_SECRET is not set.
"""
try:
    SECRET_KEY = os.getenv("FLASK_SECRET").encode("utf-8")
except AttributeError:  # pragma: no cover
    raise RuntimeError("Environment variable $FLASK_SECRET was not set")

"""SQLALCHEMY_DATABASE_URI: Database connection string.

Relative SQLite paths are resolved against the instance directory.
"""
SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI", f"sqlite:///{ENV}.db")
