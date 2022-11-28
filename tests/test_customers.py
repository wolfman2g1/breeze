import json

from fastapi.testclient import TestClient

from app import configure_app

client = TestClient(configure_app())


def test_create_customer():
    response = client.post("/api/v1/customers",
                           json={
                               "customer_name": "test3",
                               "street": "broad",
                               "state": "mine",
                               "postal": "1234"
                           }).json()
    assert response.status_code == 307
    data = response.json()
    assert data["company_name"] == "test3"
