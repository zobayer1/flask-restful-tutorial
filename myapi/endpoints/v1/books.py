# -*- coding: utf-8 -*-
from flask import Blueprint, request

from myapi.services import books as service

books_blueprint = Blueprint("books", __name__)


@books_blueprint.route("", methods=["GET"])
def list_books():
    return {"books": [book.to_dict() for book in service.list_books()]}, 200


@books_blueprint.route("/<int:book_id>", methods=["GET"])
def get_book(book_id: int):
    return service.get_book(book_id).to_dict(), 200


@books_blueprint.route("", methods=["POST"])
def create_book():
    return service.create_book(request.get_json(silent=True)).to_dict(), 201


@books_blueprint.route("/<int:book_id>", methods=["DELETE"])
def delete_book(book_id: int):
    service.delete_book(book_id)
    return "", 204
