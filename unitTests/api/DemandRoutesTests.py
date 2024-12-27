import pytest
from server import app as flask_app

@pytest.fixture
def app():
    yield flask_app

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.mark.order(1)
def test_CreateDemand(client):
    data = {
        "custom_id": 2,
        "elevator_id": 1,
        "start_floor": 3,
        "end_floor": 9,
    }
    response = client.post('/demand/create', json=data)
    assert response.status_code == 201
    assert "Success" in response.json

@pytest.mark.order(2)
def test_GetDemands(client):
    response = client.get('/demand/get')
    assert response.status_code == 200

@pytest.mark.order(3)
def test_GetDemandByElevatorId(client):
    response = client.get('/demand/get/1')
    assert response.status_code == 200

@pytest.mark.order(4)
def test_UpdateDemand(client):
    data = {
        "id": 1,
        "new_values": {
            "end_floor": 10,
            "start_floor": 4
        }
    }
    response = client.put('/demand/update', json=data)
    assert response.status_code == 200
    assert response.json == "Success"

@pytest.mark.order(5)
def test_DeleteDemand(client):
    data = {
        "id": 2
    }
    response = client.delete('/demand/delete', json=data)
    assert response.status_code == 200
    assert response.json == "Success"
