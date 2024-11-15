from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_sort_endpoint_success():
    payload = {"array": [3, 1, 2]}
    response = client.post("/api/sort", json=payload)

    assert response.status_code == 200
    assert response.json() == {"sorted_array": [1, 2, 3]}


def test_sort_endpoint_empty_array():
    payload = {"array": []}
    response = client.post("/api/sort", json=payload)

    assert response.status_code == 200
    assert response.json() == {"sorted_array": []}


def test_sort_endpoint_negative_numbers():
    payload = {"array": [10, -1, 0, 3, 5]}
    response = client.post("/api/sort", json=payload)

    assert response.status_code == 200
    assert response.json() == {"sorted_array": [-1, 0, 3, 5, 10]}


def test_sort_endpoint_invalid_payload():
    payload = {"invalid_key": [3, 1, 2]}
    response = client.post("/api/sort", json=payload)

    assert response.status_code == 422
