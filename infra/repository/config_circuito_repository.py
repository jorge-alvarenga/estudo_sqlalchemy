from infra.configs.connection import DBConnectionHandler
from infra.entities.config_circuito import Config_Circuito
from sqlalchemy.orm.exc import NoResultFound


class ConfigCircuitoRepository:

    def insert(self , Contrato, Circuito , EndPoint , SecretCompress , ReconnectTime , isActive):
        with DBConnectionHandler(Circuito) as db:
            try:
                data_isert = Config_Circuito( Contrato=Contrato, Circuito=Circuito, EndPoint = EndPoint ,
                                             SecretCompress=SecretCompress, ReconnectTime = ReconnectTime,
                                             isActive = isActive)
                db.session.add(data_isert)
                db.session.commit()
            except Exception as exception:
                db.session.rollback()
                raise exception

    def delete(self, titulo):
        with DBConnectionHandler() as db:
            try:
                db.session.query(Filmes).filter(Filmes.titulo == titulo).delete()
                db.session.commit()
            except Exception as exception:
                db.session.rollback()
                raise exception

    def update(self, titulo, ano):
        with DBConnectionHandler() as db:
            try:
                db.session.query(Filmes).filter(Filmes.titulo == titulo).update({"ano": ano})
                db.session.commit()
            except Exception as exception:
                db.session.rollback()
                raise exception