from sqlalchemy import Column, Integer, ForeignKey, Date, Time, Text, String, Float, Table, Enum
from sqlalchemy.orm import relationship
from model.utilities import Base, PaymentType

# Tornou-se necessário declarar Service e Part juntos devido a sua relação many to many.

service_part_association_table = Table('service_part_association', Base.metadata,
                                       Column('service_id', Integer, ForeignKey('service.id')),
                                       Column('part_id', Integer, ForeignKey('part.id'))
                                       )


class Service(Base):
    __tablename__ = 'service'

    id = Column(Integer, primary_key=True)
    mechanic_id = Column(Integer, ForeignKey('mechanic.id'))
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
