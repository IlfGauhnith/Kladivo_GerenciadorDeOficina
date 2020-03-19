from sqlalchemy import Column, Integer, String, ForeignKey
from model.user import User


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
