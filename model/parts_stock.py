from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship, backref
from model.utilities import Base


class PartsStock(Base):

    __tablename__ = 'parts_stock'

    id = Column(Integer, primary_key=True)
    part_id = Column(Integer, ForeignKey('part.id'))
    part = relationship("Part", backref=backref("part", uselist=False))
    quantity = Column(Integer)
