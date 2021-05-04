# -*- coding: utf-8 -*-
from flask import Blueprint
from flask_restful import Api

from myapi.health.status import ServerStatus

health_blueprint = Blueprint("health", __name__)
api = Api(health_blueprint)

api.add_resource(ServerStatus, "/status", endpoint="status")

__all__ = ["health_blueprint"]
