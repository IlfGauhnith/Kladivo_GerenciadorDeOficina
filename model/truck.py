from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, Enum
from model.utilities import MaintenancePlanTypes, Base


class Truck(Base):

    __tablename__ = 'truck'

    id = Column(Integer, primary_key=True)
    client_id = Column(Integer, ForeignKey('client.id'))
    model = Column(String(20))
    engine = Column(String(10))
    rear_axle = Column(String(10))
    license_plate = Column(String(7), unique=True)
    mileage = Column(Integer)
    is_maintenance_plan = Column(Boolean)
    maintenance_plan_type = Column(Enum(MaintenancePlanTypes), nullable=True)
