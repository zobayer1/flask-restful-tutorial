# -*- coding: utf-8 -*-
from importlib.metadata import version

from flask import Blueprint
from flask import current_app as app

health_blueprint = Blueprint("health", __name__)


@health_blueprint.route("/status", methods=["GET"])
def status():
    return {"server": f"{app.name} v{version(app.name)}", "status": "running"}, 200
