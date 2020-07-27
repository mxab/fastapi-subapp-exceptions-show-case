from fastapi.testclient import TestClient
from fastapi_subapp_exceptions_show_case.app import app


client = TestClient(app)


def test_read_main():
    response = client.get("/app")
    assert response.status_code == 418


def test_read_sub():
    response = client.get("/foo/foo")
    assert response.status_code == 418
