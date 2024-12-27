import pytest
from server import app as flask_app

@pytest.fixture
def app():
    yield flask_app

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.mark.order(1)
def test_CreateBuilding(client):
    data = {
        "custom_id": 2,
        "name": "Building A",
        "address": "Address A",
        "city": "City A",
        "country": "Country A"
    }
    response = client.post('/building/create', json=data)
    assert response.status_code == 201
    assert "Success" in response.json

@pytest.mark.order(2)
def test_GetBuildings(client):
    response = client.get('/building/get')
    assert response.status_code == 200
    assert len(response.json) > 0  # Ensure there's at least one building

@pytest.mark.order(3)
def test_GetBuildingById(client):
    response = client.get('/building/get/2')
    assert response.status_code == 200
    assert len(response.json) > 0  # Ensure the building exists

@pytest.mark.order(4)
def test_UpdateBuilding(client):
    data = {
        "id": 2,
        "new_values": {
            "country": "Updated Country"
        }
    }
    response = client.put('/building/update', json=data)
    assert response.status_code == 200
    assert response.json == "Success"

@pytest.mark.order(5)
def test_DeleteBuilding(client):
    data = {
        "id": 2
    }
    response = client.delete('/building/delete', json=data)
    assert response.status_code == 200
    assert response.json == "Success"
