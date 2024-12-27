import pytest
from models.models import Building, Elevator, Demand

def test_BuildingModelInit():
    building = Building(custom_id=1, name="Building X", address="Address X", city="City X", country="Country X")
    assert building.custom_id == 1
    assert building.name == "Building X"
    assert building.address == "Address X"
    assert building.city == "City X"
    assert building.country == "Country X"

def test_ElevatorModelInit():
    elevator = Elevator(building_id=1, highest_floor=15, elevator_number=7)
    assert elevator.building_id == 1
    assert elevator.highest_floor == 15
    assert elevator.elevator_number == 7

def test_DemandModelInit():
    demand = Demand(elevator_id=1, start_floor=3, end_floor=8)
    assert demand.elevator_id == 1
    assert demand.start_floor == 3
    assert demand.end_floor == 8
