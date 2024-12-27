from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from datetime import datetime
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Building(Base):
    __tablename__ = 'buildings'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    address = Column(String)
    city = Column(String)
    country = Column(String)

    elevators = relationship("Elevator", back_populates="building")

class Elevator(Base):
    __tablename__ = 'elevators'

    id = Column(Integer, primary_key=True)
    building_id = Column(Integer, ForeignKey('buildings.id'))
    highest_floor = Column(Integer)
    elevator_number = Column(Integer)

    building = relationship("Building", back_populates="elevators")
    demands = relationship("Demand", back_populates="elevator")

class Demand(Base):
    __tablename__ = 'demands'

    id = Column(Integer, primary_key=True)
    elevator_id = Column(Integer, ForeignKey('elevators.id'))
    start_floor = Column(Integer)
    end_floor = Column(Integer)
    timestamp = Column(DateTime, default=datetime.now)

    elevator = relationship("Elevator", back_populates="demands")
