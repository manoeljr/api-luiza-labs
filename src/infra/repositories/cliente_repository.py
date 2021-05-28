from src.infra.config import DBConnetionHandler
from src.infra.entities import Clientes
from collections import namedtuple


class ClienteRepository:
    """Cliente Repository"""

    @classmethod
    def insert_cliente(cls, nome: str, email: str) -> Clientes:
        """
        Inserindo um cliente na base de dados
        :param nome: Nome do cliente
        :param email: Email do cliente
        :return Tupla com um cliente
        """
        InsertData = namedtuple("Clientes", "id, nome, email")
        with DBConnetionHandler() as db_connection:
            try:
                cliente = Clientes(nome=nome, email=email)
                db_connection.session.add(cliente)
                db_connection.session.commit()
                return InsertData(id=cliente.id, nome=cliente.nome, email=cliente.email)
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()
