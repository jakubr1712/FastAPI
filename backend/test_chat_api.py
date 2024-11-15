from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_chat_endpoint():
    initial_history = [{"from_": "user", "message": "hello"}, {
        "from_": "bot", "message": "hello"}]
    new_message = "hello hello world"

    response = client.post(
        "/api/chat",
        json={
            "history": initial_history,
            "new_message": new_message
        }
    )

    assert response.status_code == 200
    data = response.json()
    assert "updated_history" in data

    updated_history = data["updated_history"]
    assert len(updated_history) == len(initial_history) + \
        2

    assert updated_history[-2] == {"from_": "user", "message": new_message}
    assert updated_history[-1] == {"from_": "bot",
                                   "message": "hello fake world"}
