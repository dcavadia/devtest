from typing import Dict, Any, Tuple
from flask import jsonify, Response
from utils.db import PostgreSQLHandler
from models.models import Demand
from utils.serializer import serialize_model

class DemandController:
    @staticmethod
    def Create(data: Dict[str, Any]) -> Tuple[str, int]:
        new_demand = Demand(**data)
        return DemandController._ExecuteDbOperation(PostgreSQLHandler().create, new_demand, 201)

    @staticmethod
    def Get(elevator_id: int = None) -> Response:
        filter_by = {"elevator_id": elevator_id} if elevator_id else None
        demands = PostgreSQLHandler().read(Demand, filter_by=filter_by)
        return jsonify([serialize_model(demand) for demand in demands])

    @staticmethod
    def Update(data: Dict[str, Any]) -> Tuple[str, int]:
        return DemandController._ExecuteDbOperation(
            PostgreSQLHandler().update,
            Demand,
            {"id": data["id"]},
            data["new_values"]
        )

    @staticmethod
    def Delete(data: Dict[str, Any]) -> Tuple[str, int]:
        return DemandController._ExecuteDbOperation(PostgreSQLHandler().delete, Demand, data)

    @staticmethod
    def _ExecuteDbOperation(operation, *args) -> Tuple[str, int]:
        result = operation(*args)
        status_code = 201 if "Success" in result and operation.__name__ == 'create' else 200
        status_code = 500 if "sql" in result.lower() else status_code
        return result, status_code
