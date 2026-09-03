# -*- coding: utf-8 -*-
from myapi.commons.errors import BadRequest, NotFound
from myapi.extensions import db
from myapi.models import Book

REQUIRED_FIELDS = ("title", "author", "year")


def list_books() -> list:
    return db.session.scalars(db.select(Book).order_by(Book.id)).all()


def get_book(book_id: int) -> Book:
    book = db.session.get(Book, book_id)
    if book is None:
        raise NotFound(f"Book {book_id} does not exist")
    return book


def create_book(payload: dict) -> Book:
    if not isinstance(payload, dict):
        raise BadRequest("Request body must be a JSON object")
    missing = [field for field in REQUIRED_FIELDS if field not in payload]
    if missing:
        raise BadRequest(f"Missing required fields: {', '.join(missing)}")
    if not isinstance(payload["year"], int):
        raise BadRequest("Field 'year' must be an integer")
    book = Book(title=payload["title"], author=payload["author"], year=payload["year"])
    db.session.add(book)
    db.session.commit()
    return book


def delete_book(book_id: int):
    book = get_book(book_id)
    db.session.delete(book)
    db.session.commit()
