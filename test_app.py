import pytest
from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    return app.test_client()


def test_ping(client):
    response = client.get("/ping")

    assert response.status_code == 200
    assert response.json["message"] == "MLOps API is running!"


def test_greet(client):
    response = client.get("/greet?name=Suhasini")

    assert response.status_code == 200
    assert response.json["message"] == "Hello, Suhasini!"


def test_sum(client):
    response = client.post(
        "/sum",
        json={"a": 10, "b": 20}
    )

    assert response.status_code == 200
    assert response.json["sum"] == 30