# -*- coding: utf-8 -*-
import os

import pytest

from myapi.app import create_app


@pytest.fixture(scope="module")
def app():
    """A flask app with testing configurations"""
    os.environ.update(
        {
            "FLASK_ENV": "testing",
            "FLASK_SECRET": "bb9ba2817ef62e261d3adaf90c2727bb",
            "LOGGING_ROOT": ".",
        }
    )
    return create_app("testing")


@pytest.fixture(scope="module")
def client(app):
    """An HTTP test client to test api endpoints"""
    return app.test_client()


@pytest.fixture(scope="module")
def runner(app):
    """A CLI test client to test shell commands"""
    return app.test_cli_runner()
