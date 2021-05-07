# -*- coding: utf-8 -*-
from importlib.metadata import version

from flask import current_app as app
from flask_restful import Resource


class ServerStatus(Resource):
    # noinspection PyMethodMayBeStatic
    def get(self):
        return {"server": f"{app.name} v{version(app.name)}", "status": "running"}, 200
