from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, backref
from model.utilities import Base


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
        'polymorphic_identity':'company'
    }
