# -*- coding: utf-8 -*-
import sys


def app_version(name: str) -> str:
    if sys.version_info < (3, 8):  # pragma: no cover
        # noinspection PyUnresolvedReferences
        from importlib_metadata import version
    else:  # pragma: no cover
        from importlib.metadata import version
    return version(name)
