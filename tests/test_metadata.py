# -*- coding: utf-8 -*-
from importlib.metadata import version


def test_application_version():
    """Test fails if version can not be loaded from metadata"""
    assert version("myapi")
