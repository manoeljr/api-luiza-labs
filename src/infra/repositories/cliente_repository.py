from src.infra.config import DBConnetionHandler
from src.infra.entities import Clientes as clienteModel
from src.domain.models import Clientes


class ClienteRepository:
    """Cliente Repository"""

    @classmethod
    def insert_cliente(cls, nome: str, email: str) -> ClienteModel:
        """
        Inserindo um cliente na base de dados
        :param nome: Nome do cliente
        :param email: Email do cliente
        :return Tupla com um cliente
        """
        
        with DBConnetionHandler() as db_connection:
            try:
                cliente = ClienteModel(nome=nome, email=email)
                db_connection.session.add(cliente)
                db_connection.session.commit()
                return Clientes(id=cliente.id, nome=cliente.nome, email=cliente.email)
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()
