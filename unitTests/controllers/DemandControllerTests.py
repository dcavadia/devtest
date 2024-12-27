import pytest
from flask import Flask
from controllers.demand_controllers import DemandController

#Mock
app = Flask(__name__)

@pytest.mark.order(1)
def test_CreateDemand():
    data = {
        "custom_id": 1,
        "elevator_id": 1,
        "start_floor": 3,
        "end_floor": 8,
    }
    result, status_code = DemandController.Create(data)
    assert status_code == 201
    assert "Success" in result

#Assuming there are demands
@pytest.mark.order(2)
def test_GetDemands():
    """Assuming there are demands in the database for testing."""
    with app.test_request_context():
        elevator_id = 1
        response = DemandController.Get(elevator_id)
    assert response.status_code == 200

@pytest.mark.order(3)
def test_UpdateDemand():
    data = {"id": 1, "new_values": {"start_floor": 4, "end_floor": 9}}
    result, status_code = DemandController.Update(data)
    assert result == "Success"
    assert status_code == 200

@pytest.mark.order(4)
def test_DeleteDemand():
    data = {"id": 1}
    result, status_code = DemandController.Delete(data)
    assert result == "Success"
    assert status_code == 200
