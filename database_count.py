from sqlalchemy import Column, String, Integer, Boolean, DateTime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Config_Circuito(Base):
    __tablename__ = "Contagem"
    id = Column(Integer, primary_key=True)
    #circuito = Column(String, nullable=False)
    dt_insert = Column(String, nullable=False)
    camera_id = Column(String, nullable=False)
    bound_box = Column(String, nullable=False)
    count = Column(Integer, nullable=False)
    upload = Column(Boolean, nullable=False)

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

class ConfigCircuitoRepository:
    def insert(self ,circuito, dt_insert, camera_id , bound_box , count , upload ):
        with DBConnectionHandler(circuito) as db:
            try:
                data_insert = Config_Circuito( dt_insert=dt_insert,
                                              camera_id=camera_id, bound_box=bound_box,
                                              count=count, upload=upload)

                db.session.add(data_insert)
                db.session.commit()
            except Exception as exception:
                db.session.rollback()
                raise exception
