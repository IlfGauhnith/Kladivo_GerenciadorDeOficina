from sqlalchemy import Column, Integer, String, Enum
from model.utilities import Base, AccessLevel


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
