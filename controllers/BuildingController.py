from typing import Dict, Any, Tuple
from flask import jsonify, Response
from utils.db import PostgreSQLHandler
from models.models import Building
from utils.serializer import serialize_model

class BuildingController:
    @staticmethod
    def Create(data: Dict[str, Any]) -> Tuple[str, int]:
        new_building = Building(**data)
        return BuildingController._ExecuteDbOperation(PostgreSQLHandler().create, new_building, 201)

    @staticmethod
    def Get(building_data: Dict[str, Any] = None) -> Response:
        buildings = PostgreSQLHandler().read(Building, filter_by=building_data)
        return jsonify([serialize_model(building) for building in buildings])

    @staticmethod
    def Update(data: Dict[str, Any]) -> Tuple[str, int]:
        return BuildingController._ExecuteDbOperation(
            PostgreSQLHandler().update,
            Building,
            {"id": data["id"]},
            data["new_values"]
        )

    @staticmethod
    def Delete(data: Dict[str, Any]) -> Tuple[str, int]:
        return BuildingController._ExecuteDbOperation(PostgreSQLHandler().delete, Building, data)

    @staticmethod
    def _ExecuteDbOperation(operation, *args) -> Tuple[str, int]:
        result = operation(*args)
        status_code = 201 if "Success" in result and operation.__name__ == 'create' else 200
        status_code = 500 if "sql" in result.lower() else status_code
        return result, status_code
