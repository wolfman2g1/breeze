import json

from fastapi.testclient import TestClient

from app import configure_app

client = TestClient(configure_app())


def test_create_tech():
    data = {
        "fname": "joe",
        "lname": "smith",
        "password": "test1",
        "email": "abc@1234.com",
        "admin": True
    }

    response = client.post("/api/v1/techs", json.dumps(data))
    # assert response.status_code == 201
    assert response.json()["fname"] == "joe"
    assert response.json()["lname"] == "bob"
    assert response.json()["email"] == "abc@12344.com"
    assert response.json()["admin"] == True


def test_get_techs():
    response = client.get("/api/v1/techs")
    assert response.status_code == 200
