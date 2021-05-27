from src.infra.config import DBConnetionHandler
from src.infra.entities import Clientes


class FakeRepository:
    """ Repositorio de teste(insert, select, delete, update) na base de dados """

    @classmethod
    def insert_cliente(cls):
        with DBConnetionHandler() as db_connection:
            try:
                cliente = Clientes(
                    nome="Primeiro cliente", email="primeirocliente@gmail.com"
                )
                db_connection.session.add(cliente)
                db_connection.session.commit()
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()
