from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from infra.configs.base import Base
class DBConnectionHandler:
    def __init__(self, circuito) -> None:

        self._circuito = circuito
        self.__connection_database = self.__create_connection_database()
        self.__engine = self.__create_database_engine()
        self.session = None


    def __create_connection_database(self):
        data_atual_formatada = datetime.now().strftime("%Y%m%d")
        self.database = f'sqlite:///{self._circuito}_{data_atual_formatada}.db'
        return self.database

    def __create_database_engine(self):
        engine = create_engine(self.__connection_database)
        Base.metadata.create_all(engine)
        return engine

    def get_engine(self):
        return self.__engine

    def __enter__(self):
        session_maker = sessionmaker(bind=self.__engine)
        self.session = session_maker()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.session:
            self.session.close()