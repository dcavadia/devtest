import pytest
from server import app as flask_app

@pytest.fixture
def app():
    yield flask_app

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.mark.order(1)
def test_CreateElevator(client):
    data = {
        "custom_id": 2,
        "building_id": 1,
        "max_floors": 15, 
        "local_identifier": 7
    }
    response = client.post('/elevator/create', json=data)
    assert response.status_code == 201
    assert "Success" in response.json

@pytest.mark.order(2)
def test_GetElevators(client):
    response = client.get('/elevator/get')
    assert response.status_code == 200

@pytest.mark.order(3)
def test_GetElevatorByBuildingId(client):
    response = client.get('/elevator/get/1')
    assert response.status_code == 200

@pytest.mark.order(4)
def test_UpdateElevator(client):
    data = {
        "id": 1,
        "new_values": {
            "local_identifier": 8,
            "highest_floor": 20
        }
    }
    response = client.put('/elevator/update', json=data)
    assert response.status_code == 200
    assert response.json == "Success"

@pytest.mark.order(5)
def test_DeleteElevator(client):
   data = {
       "id": 2
   }
   response = client.delete('/elevator/delete', json=data)
   assert response.status_code == 200
   assert response.json == "Success"
