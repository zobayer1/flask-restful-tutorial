# -*- coding: utf-8 -*-
import json


def test_server_status_returns_success(client):
    """Test fails if /myapi/health/status does not return success"""
    response = client.get("/myapi/health/status")
    assert response.status_code == 200
    assert json.loads(response.data).get("status") == "running"
