from fastapi.testclient import TestClient
from main import app


fake_player_db = {
    1: { "id": 1, "name": "player", "lvl": 1, "expMax": 100, "expCurr": 0, "hp": 10, "mp": 10, "atk": 1, "defn": 1, "spd": 10},
    2: { "id": 2, "name": "player2", "lvl": 10, "expMax": 10000, "expCurr": 300, "hp": 100, "mp": 50, "atk": 3, "defn": 2, "spd": 50},
    3: { "id": 3, "name": "player3", "lvl": 1, "expMax": 100, "expCurr": 0, "hp": 10, "mp": 10, "atk": 1, "defn": 1, "spd": 10},
}


def test_read_root():
    client = TestClient(app)
    response = client.get("/")
    assert response.status_code == 200
    assert response.text == "player"


def test_create_player():
    client = TestClient(app)
    response = client.post("/player", json={"name": "player"})
    assert response.status_code == 201
    assert response.json() == {
        "id": 1,
        "name": "testo0"
    }


def test_read_players():
    client = TestClient(app)
    response = client.get("/players")
    assert response.status_code == 200


def test_read_player():
    client = TestClient(app)
    response = client.get("/player/1")
    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "player"}


def test_read_player_with_name():
    client = TestClient(app)
    response = client.get("/player/player")
    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "player"}


def test_update_player():
    client = TestClient(app)
    response = client.put("/player/1", json={"name": "player"})
    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "player"}


def test_update_player_with_name():
    client = TestClient(app)
    response = client.put("/player/player", json={"name": "player"})
    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "player"}


def delete_player():
    client = TestClient(app)
    response = client.delete("/player/1")
    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "player"}


def delete_player_with_name():
    client = TestClient(app)
    response = client.delete("/player/player")
    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "player"}


def test_read_player_not_found():
    client = TestClient(app)
    response = client.get("/player/4")
    assert response.status_code == 404
    assert response.json() == {"detail": "player  with id 4 not found"}


def test_read_player_with_name_not_found():
    client = TestClient(app)
    response = client.get("/player/player4")
    assert response.status_code == 404
    assert response.json() == {"detail": "player  with name player4 not found"}


def test_update_player_not_found():
    client = TestClient(app)
    response = client.put("/player/4", json={"name": "player4"})
    assert response.status_code == 404
    assert response.json() == {"detail": "player  with id 4 not found"}


def test_update_player_with_name_not_found():
    client = TestClient(app)
    response = client.put("/player/player4", json={"name": "player4"})
    assert response.status_code == 404
    assert response.json() == {"detail": "player  with name player4 not found"}


def test_delete_player_not_found():
    client = TestClient(app)
    response = client.delete("/player/4")
    assert response.status_code == 404
    assert response.json() == {"detail": "player  with id 4 not found"}


def test_delete_player_with_name_not_found():
    client = TestClient(app)
    response = client.delete("/player/player4")
    assert response.status_code == 404
    assert response.json() == {"detail": "player  with name player4 not found"}
