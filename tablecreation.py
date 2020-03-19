"""from sqlalchemy import (Column,
                        Integer,
                        String,
                        ForeignKey,
                        Enum,
                        Float,
                        Date,
                        Time,
                        Table,
                        Text,
                        Boolean)
from sqlalchemy.orm import relationship, backref
from data.SQLAlchemy_data_source import SQLAlchemyDataSource
from model.utilities import Base, PaymentType, MaintenancePlanTypes, AccessLevel

db = SQLAlchemyDataSource()
db_engine = db.engine


class Client(Base):

    __tablename__ = 'client'

    id = Column(Integer, primary_key=True)
    polymorphic_type = Column(String(50))
    email = Column(String(35))
    telephone1 = Column(String(11))
    telephone2 = Column(String(11), nullable=True)
    fleet = relationship("Truck")
    address_id = Column(Integer, ForeignKey('address.id'))
    address = relationship("Address", backref=backref("client", uselist=False))

    __mapper_args__ = {
        'polymorphic_identity':'client',
        'polymorphic_on': polymorphic_type
    }


class Customer(Client):

    __tablename__ = 'customer'

    id = Column(Integer, ForeignKey('client.id'), primary_key=True)
    name = Column(String(50))
    cpf = Column(String(11), unique=True)

    __mapper_args__ = {
        'polymorphic_identity':'customer'
    }


class Company(Client):

    __tablename__ = 'company'

    id = Column(Integer, ForeignKey('client.id'), primary_key=True)
    company_name = Column(String(150))
    cnpj = Column(String(14), unique=True)

    __mapper_args__ = {
        'polymorphic_identity': 'company'
    }


class Address(Base):

    __tablename__ = 'address'

    id = Column(Integer, primary_key=True)
    street = Column(String(60))
    zip_code = Column(String(8))
    province = Column(String(2))
    city = Column(String(20))
    complement = Column(String(100), nullable=True)
    number = Column(String(10), nullable=True)


class User(Base):

    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    login = Column(String(25), unique=True)
    password = Column(String(150))                  # Senha será encriptada.
    access_level = Column(Enum(AccessLevel))
    polymorphic_type = Column(String(50))
    __mapper_args__ = {
        'polymorphic_identity': 'user',
        'polymorphic_on': polymorphic_type
    }


class Employee(User):

    __tablename__ = 'employee'

    id = Column(Integer, ForeignKey('user.id'), primary_key=True)
    name = Column(String(50), primary_key=True)
    polymorphic_type = Column(String(50))

    # No db será arquivo o path dentro do sistema, da foto do funcionário. As fotos propriamente
    # ditas seram arquivadas na pasta resources\images\user_profiles
    photo_file_path = Column(String(50), primary_key=True, default='')

    __mapper_args__ = {
        'polymorphic_identity': 'employee',
        'polymorphic_on': polymorphic_type
    }

class Mechanic(Employee):

    __tablename__ = 'mechanic'

    id = Column(Integer, ForeignKey('employee.id'), primary_key=True)
    services = relationship("Service")

    __mapper_args__ = {
        'polymorphic_identity': 'mechanic'
    }


class PartsStock(Base):

    __tablename__ = 'parts_stock'

    id = Column(Integer, primary_key=True)
    part_id = Column(Integer, ForeignKey('part.id'))
    part = relationship("Part", backref=backref("part", uselist=False))
    quantity = Column(Integer)


# Tornou-se necessário declarar Service e Part juntos devido a sua relação many to many.

service_part_association_table = Table('service_part_association', Base.metadata,
                                       Column('service_id', Integer, ForeignKey('service.id')),
                                       Column('part_id', Integer, ForeignKey('part.id'))
                                       )


class Service(Base):

    __tablename__ = 'service'

    id = Column(Integer, primary_key=True)
    mechanic_id = Column(Integer, ForeignKey('mechanic.id'))
    truck_id = Column(Integer, ForeignKey('truck.id'))
    truck = relationship("Truck", backref=backref("service", uselist=False))
    entry_date = Column(Date)
    entry_time = Column(Time)
    delivery_prevision_date = Column(Date)
    delivery_prevision_hour = Column(Time)
    effective_delivered_date = Column(Date)
    effective_delivered_hour = Column(Time)
    service_description = Column(Text)
    used_parts = relationship("Part", secondary=service_part_association_table)
    total_charge = Column(Float(5))
    payment_type = Column(Enum(PaymentType))


class Part(Base):
    __tablename__ = 'part'

    id = Column(Integer, primary_key=True)
    name = Column(String(40))
    description = Column(String(40))
    price = Column(Float(5))
    ean13 = Column(String(13), unique=True)

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


Base.metadata.create_all(db_engine)"""
