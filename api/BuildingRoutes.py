from flask import Blueprint, jsonify, request
from controllers.building_controllers import BuildingController

building_blueprint = Blueprint('building', __name__)

@building_blueprint.route('/get', defaults={'building_id': None}, methods=['GET'])
@building_blueprint.route('/get/<int:building_id>', methods=['GET'])
def GetBuildings(building_id):
    data = {"id": building_id} if building_id else None
    return BuildingController.get(data)

@building_blueprint.route('/create', methods=['POST'])
def CreateBuilding():
    required_keys = ["name", "address", "city", "country"]
    if not all(key in request.json for key in required_keys):
        return jsonify({'error': 'Building name, address, city, and country are required'}), 400
    return BuildingController.create(request.json)

@building_blueprint.route('/update', methods=['PUT'])
def UpdateBuilding():
    required_keys = ["id", "new_values"]
    if not all(key in request.json for key in required_keys):
        return jsonify({'error': 'Building ID and new_values are required'}), 400
    return BuildingController.update(request.json)

@building_blueprint.route('/delete', methods=['DELETE'])
def DeleteBuilding():
    if "id" not in request.json:
        return jsonify({'error': 'Building ID is required for deletion'}), 400
    return BuildingController.delete(request.json)
