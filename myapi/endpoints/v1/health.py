# -*- coding: utf-8 -*-
from flask import Blueprint
from flask import current_app as app

from myapi.commons.helpers.metadata import app_version

health_blueprint = Blueprint("health", __name__)


@health_blueprint.route("/status", methods=["GET"])
def status():
    return {"server": f"{app.name} v{app_version(app.name)}", "status": "running"}, 200
