from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class SQLAlchemyDataSource(object):

    """
    Nesta classe utilizo o padrão de projeto Singleton.
    """
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(SQLAlchemyDataSource, cls).__new__(cls)

        return cls._instance

    def __init__(self):
        self.__user = 'root'
        self.__password = 'root'
        self.__host = 'localhost'
        self.__port = '3306'
        self.__database_name = 'oficinadb'
        self.__engine = create_engine('mysql+mysqlconnector://' + self.__user + ':' + self.__password + '@'
                               + self.__host + ':' + self.__port + '/' + self.__database_name, echo=True)

    def get_session(self):
        Session = sessionmaker(bind=self.__engine)
        session = Session()

        return session
