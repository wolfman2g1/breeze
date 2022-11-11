from fastapi.testclient import TestClient

from app import configure_app

client = TestClient(configure_app())

def test_ping():
    response = client.get("/api/v1/ping")
    assert response.status_code == 200
    assert response.json() == {"message": "PONG!"}