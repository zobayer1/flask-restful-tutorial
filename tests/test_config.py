# -*- coding: utf-8 -*-
from myapi.commons.helpers.metadata import app_version


def test_env(app):
    """Test fails if app was not initialized with testing configurations"""
    assert app.config["ENV"] == "testing"
    assert app.testing


def test_application_version(app):
    """Test fails if importlib metadata could not be loaded from metadata"""
    assert app.name == "myapi"
    assert len(app_version(app.name)) > 0
