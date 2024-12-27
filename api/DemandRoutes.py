from flask import Blueprint, jsonify, request
from controllers.demand_controllers import DemandController

demand_blueprint = Blueprint('demand', __name__)

@demand_blueprint.route('/get', defaults={'elevator_id': None}, methods=['GET'])
@demand_blueprint.route('/get/<int:elevator_id>', methods=['GET'])
def GetDemands(elevator_id):
    return DemandController.get(elevator_id)

@demand_blueprint.route('/create', methods=['POST'])
def CreateDemand():
    required_keys = ["elevator_id", "start_floor", "end_floor"]
    if not all(key in request.json for key in required_keys):
        return jsonify({'error': 'elevator_id, start_floor, and end_floor are required'}), 400
    return DemandController.create(request.json)

@demand_blueprint.route('/update', methods=['PUT'])
def UpdateDemand():
    required_keys = ["id", "new_values"]
    if not all(key in request.json for key in required_keys):
        return jsonify({'error': 'Demand ID and new_values are required'}), 400
    return DemandController.update(request.json)

@demand_blueprint.route('/delete', methods=['DELETE'])
def DeleteDemand():
    if "id" not in request.json:
        return jsonify({'error': 'Demand ID is required for deletion'}), 400
    return DemandController.delete(request.json)
