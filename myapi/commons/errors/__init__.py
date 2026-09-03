# -*- coding: utf-8 -*-
from flask import Flask


class APIError(Exception):
    """Base class for errors that render as a JSON response"""

    status_code = 500
    message = "Internal server error"

    def __init__(self, message: str = None):
        super().__init__(message or self.message)
        if message:
            self.message = message

    def to_dict(self) -> dict:
        return {"error": self.message, "status": self.status_code}


class BadRequest(APIError):
    status_code = 400
    message = "Bad request"


class NotFound(APIError):
    status_code = 404
    message = "Resource not found"


class Conflict(APIError):
    status_code = 409
    message = "Resource already exists"


def register_error_handlers(app: Flask):
    """Registers a single handler for every APIError subclass"""

    @app.errorhandler(APIError)
    def handle_api_error(error: APIError):
        return error.to_dict(), error.status_code
