import os
from sqlalchemy import create_engine, inspect
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker
from sqlalchemy.schema import CreateTable
from models.models import Base
from typing import Any, List, Dict

TABLES = ["buildings", "elevators", "demands"]

class DatabaseManager:
    def __init__(self):
        url = (
            f'postgresql://{os.getenv("DB_USERNAME")}:{os.getenv("DB_PASSWORD")}@'
            f'{os.getenv("DB_HOST")}/{os.getenv("DB_NAME")}'
        )
        self.engine = create_engine(url)
        self.session = sessionmaker(bind=self.engine)()
        self._inspector = inspect(self.engine)

    def _CreateTable(self, table_name: str) -> None:
        if not self._inspector.has_table(table_name):
            table_obj = Base.metadata.tables.get(table_name)
            if table_obj:
                with self.engine.connect() as connection:
                    connection.execute(CreateTable(table_obj))
                print(f"Table {table_name} created successfully.")
            else:
                print(f"Error: Table {table_name} definition not found.")

    def EraseTables(self) -> None:
        print("Erasing tables...")
        Base.metadata.drop_all(self.engine, [Base.metadata.tables.get(table) for table in TABLES], checkfirst=True)
        print("Tables erased.")

    def InitDb(self) -> None:
        for table in TABLES:
            self._CreateTable(table)

    def Create(self, obj: Any) -> str:
        return self._ExecuteDbOperation(lambda: self.session.add(obj))

    def Read(self, obj: Any, filter_by: Dict[str, Any] = None) -> List[Any]:
        query = self.session.query(obj).filter_by(**filter_by).all() if filter_by else self.session.query(obj).all()
        return query

    def Update(self, obj: Any, filter_by: Dict[str, Any], values: Dict[str, Any]) -> str:
        query = self.Read(obj, filter_by)
        if not query:
            return "No matching records found for update"
        
        for key, value in values.items():
            setattr(query[0], key, value)
        
        return self._ExecuteDbOperation(lambda: None)

    def Delete(self, obj: Any, filter_by: Dict[str, Any] = None) -> str:
        query = self.Read(obj, filter_by)
        if not query:
            return "No matching records found for delete"
        
        return self._ExecuteDbOperation(lambda: self.session.delete(query[0]))

    def _ExecuteDbOperation(self, operation) -> str:
        try:
            operation()
            self.session.commit()
            return "Success"
        except SQLAlchemyError as e:
            return str(e.__dict__.get('orig', 'An error occurred'))

    #Serialize a SQLAlchemy model instance to a dictionary."""
    def SerializeModel(self, instance: Any, nested: bool = True) -> Dict[str, Any]:
        serialized = {key: getattr(instance, key) for key in instance.__mapper__.c.keys()}

        if nested:
            for relationship in instance.__mapper__.relationships:
                related_instance = getattr(instance, relationship.key)
                if isinstance(related_instance, list):
                    serialized[relationship.key] = [self.SerializeModel(item) for item in related_instance]
                elif related_instance and getattr(related_instance, "__mapper__", None):
                    serialized[relationship.key] = self.SerializeModel(related_instance)

        return serialized
