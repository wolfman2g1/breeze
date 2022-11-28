import json

from fastapi.testclient import TestClient

from app import configure_app

client = TestClient(configure_app())


def test_create_tech():
    data = {
        "fname": "joe",
        "lname": "smifth",
        "password": "eetest1",
        "email": "abc@1ggfeegghh55rr23wwwr4.com",
        "admin": True
    }

    response = client.post("/api/v1/techs", data=json.dumps(data)).json()
    # assert response.status_code == 201
    assert response['email'] == "abc@1ggfeegghh55rr23wwwr4.com"


def test_get_techs():
    response = client.get("/api/v1/techs")
    assert response.status_code == 200
