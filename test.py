from data.SQLAlchemy_data_source import SQLAlchemyDataSource
from data.data_handlers import AddressDataHandler, CustomerDataHandler, MechanicDataHandler
from model import Address

db = SQLAlchemyDataSource()
session = db.get_session()