import pytest
from flask import Flask
from controllers.elevator_controllers import ElevatorController

#Mock
app = Flask(__name__)

@pytest.mark.order(1)
def test_CreateElevator():
    data = {
        "custom_id": 1,
        "building_id": 1,
        "max_floors": 15, 
        "local_identifier": 7
    }
    result, status_code = ElevatorController.Create(data)
    assert status_code == 201
    assert "Success" in result

#Assuming there are elevators
@pytest.mark.order(2)
def test_GetElevators():
    with app.test_request_context():
        building_id = 1
        response = ElevatorController.Get(building_id)
    assert response.status_code == 200

@pytest.mark.order(3)
def test_UpdateElevator():
    data = {"id": 1, "new_values": {"local_identifier": 4, "highest_floor": 20}}
    result, status_code = ElevatorController.Update(data)
    assert result == "Success"
    assert status_code == 200

@pytest.mark.order(4)
def test_DeleteElevator():
    data = {"id": 1}
    result, status_code = ElevatorController.Delete(data)
    assert result == "Success"
    assert status_code == 200
