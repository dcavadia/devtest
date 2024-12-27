from flask import Blueprint, jsonify, request
from controllers.elevator_controllers import ElevatorController

elevator_blueprint = Blueprint('elevator', __name__)

@elevator_blueprint.route('/get', defaults={'building_id': None}, methods=['GET'])
@elevator_blueprint.route('/get/<int:building_id>', methods=['GET'])
def GetElevators(building_id):
    return ElevatorController.get(building_id)

@elevator_blueprint.route('/create', methods=['POST'])
def CreateElevator():
    required_keys = ["building_id", "max_floors", "local_identifier"]
    if not all(key in request.json for key in required_keys):
        return jsonify({'error': 'Building ID, max_floors, and local_identifier are required'}), 400
    return ElevatorController.create(request.json)

@elevator_blueprint.route('/update', methods=['PUT'])
def UpdateElevator():
    required_keys = ["id", "new_values"]
    if not all(key in request.json for key in required_keys):
        return jsonify({'error': 'Elevator ID and new_values are required'}), 400
    return ElevatorController.update(request.json)

@elevator_blueprint.route('/delete', methods=['DELETE'])
def DeleteElevator():
    if "id" not in request.json:
        return jsonify({'error': 'Elevator ID is required for deletion'}), 400
    return ElevatorController.delete(request.json)
