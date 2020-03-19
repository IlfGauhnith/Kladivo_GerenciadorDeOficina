from sqlalchemy import Column, Integer, String
from model.utilities import Base


class Address(Base):

    __tablename__ = 'address'

    id = Column(Integer, primary_key=True)
    street = Column(String(60))
    zip_code = Column(String(8))
    province = Column(String(2))
    city = Column(String(20))
    complement = Column(String(100), nullable=True)
    number = Column(String(10), nullable=True)
