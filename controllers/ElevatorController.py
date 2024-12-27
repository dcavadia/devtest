from typing import Dict, Any, Tuple
from flask import jsonify, Response
from utils.db import PostgreSQLHandler
from models.models import Elevator
from utils.serializer import serialize_model

class ElevatorController:
    @staticmethod
    def Create(data: Dict[str, Any]) -> Tuple[str, int]:
        new_elevator = Elevator(**data)
        return ElevatorController._ExecuteDbOperation(PostgreSQLHandler().create, new_elevator, 201)

    @staticmethod
    def Get(elevator_id: int = None) -> Response:
        filter_by = {"id": elevator_id} if elevator_id else None
        elevators = PostgreSQLHandler().read(Elevator, filter_by=filter_by)
        return jsonify([serialize_model(elevator) for elevator in elevators])

    @staticmethod
    def Update(data: Dict[str, Any]) -> Tuple[str, int]:
        return ElevatorController._ExecuteDbOperation(
            PostgreSQLHandler().update,
            Elevator,
            {"id": data["id"]},
            data["new_values"]
        )

    @staticmethod
    def Delete(data: Dict[str, Any]) -> Tuple[str, int]:
        return ElevatorController._ExecuteDbOperation(PostgreSQLHandler().delete, Elevator, data)

    @staticmethod
    def _ExecuteDbOperation(operation, *args) -> Tuple[str, int]:
        result = operation(*args)
        status_code = 201 if "Success" in result and operation.__name__ == 'create' else 200
        status_code = 500 if "sql" in result.lower() else status_code
        return result, status_code
