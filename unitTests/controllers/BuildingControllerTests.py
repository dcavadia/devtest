import pytest
from flask import Flask
from controllers.building_controllers import BuildingController

#Mock
app = Flask(__name__)

@pytest.mark.order(1)
def test_CreateBuilding():
    data = {
        "custom_id": 1,
        "name": "Building X",
        "address": "Address X",
        "city": "City X",
        "country": "Country X"
    }
    result, status_code = BuildingController.Create(data)
    assert status_code == 201
    assert "Success" in result

#Assuming there are buildings
@pytest.mark.order(2)
def test_GetBuildings():
    with app.test_request_context():
        building_data = {"name": "Building X"}
        response = BuildingController.Get(building_data)
    assert response.status_code == 200

@pytest.mark.order(3)
def test_UpdateBuilding():
    data = {"id": 1, "new_values": {"address": "New Address Y", "city": "New City Y"}}
    result, status_code = BuildingController.Update(data)
    assert result == "Success"
    assert status_code == 200

@pytest.mark.order(4)
def test_DeleteBuilding():
    data = {"id": 1}
    result, status_code = BuildingController.Delete(data)
    assert result == "Success"
    assert status_code == 200
