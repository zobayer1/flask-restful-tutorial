# -*- coding: utf-8 -*-
import json

PAYLOAD = {"title": "Dune", "author": "Frank Herbert", "year": 1965}


def create(client, **overrides):
    payload = {**PAYLOAD, **overrides}
    return client.post("/myapi/v1/books", json=payload)


def test_create_book_returns_created(client):
    """Test fails if a valid payload is not persisted"""
    response = create(client)
    assert response.status_code == 201
    body = json.loads(response.data)
    assert body["title"] == "Dune"
    assert body["status"] == "available"
    assert body["id"] > 0


def test_list_books_returns_collection(client):
    """Test fails if the created book is not listed"""
    create(client, title="Children of Dune")
    response = client.get("/myapi/v1/books")
    assert response.status_code == 200
    titles = [book["title"] for book in json.loads(response.data)["books"]]
    assert "Children of Dune" in titles


def test_get_book_returns_one(client):
    """Test fails if a book cannot be fetched by id"""
    book_id = json.loads(create(client, title="Messiah").data)["id"]
    response = client.get(f"/myapi/v1/books/{book_id}")
    assert response.status_code == 200
    assert json.loads(response.data)["title"] == "Messiah"


def test_get_missing_book_returns_not_found(client):
    """Test fails if a missing book does not raise NotFound"""
    response = client.get("/myapi/v1/books/4041")
    assert response.status_code == 404
    assert json.loads(response.data) == {"error": "Book 4041 does not exist", "status": 404}


def test_create_book_without_required_fields_returns_bad_request(client):
    """Test fails if missing fields are not reported"""
    response = client.post("/myapi/v1/books", json={"title": "Dune"})
    assert response.status_code == 400
    assert "author" in json.loads(response.data)["error"]


def test_create_book_with_non_integer_year_returns_bad_request(client):
    """Test fails if the year is not type checked"""
    response = create(client, year="1965")
    assert response.status_code == 400
    assert json.loads(response.data)["status"] == 400


def test_delete_book_removes_it(client):
    """Test fails if a deleted book is still reachable"""
    book_id = json.loads(create(client, title="Heretics").data)["id"]
    assert client.delete(f"/myapi/v1/books/{book_id}").status_code == 204
    assert client.get(f"/myapi/v1/books/{book_id}").status_code == 404


def test_create_book_without_json_body_returns_bad_request(client):
    """Test fails if a non JSON body is not rejected"""
    response = client.post("/myapi/v1/books", data="not json")
    assert response.status_code == 400
    assert json.loads(response.data)["error"] == "Request body must be a JSON object"
