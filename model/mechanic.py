from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship, backref
from model.employee import Employee


class Mechanic(Employee):

    __tablename__ = 'mechanic'

    id = Column(Integer, ForeignKey('employee.id'), primary_key=True)
    services = relationship("Service")

    __mapper_args__ = {
        'polymorphic_identity': 'mechanic'
    }
