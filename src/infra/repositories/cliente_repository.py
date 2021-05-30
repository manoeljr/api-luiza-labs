from src.infra.config import DBConnetionHandler
from src.infra.entities import Clientes as clienteModel
from src.data.interfaces import ClienteRepositoryInterfaces
from src.domain.models import Clientes
from typing import Dict


class ClienteRepository(ClienteRepositoryInterfaces):
    """Cliente Repository"""

    @classmethod
    def insert_cliente(cls, nome: str, email: str) -> Clientes:
        """
        Inserindo um cliente na base de dados
        :param nome: Nome do cliente
        :param email: Email do cliente
        :return Tupla com um cliente
        """
        with DBConnetionHandler() as db_connection:
            try:
                cliente = clienteModel(nome=nome, email=email)
                db_connection.session.add(cliente)
                db_connection.session.commit()
                return Clientes(id=cliente.id, nome=cliente.nome, email=cliente.email)
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()

    @classmethod
    def select_cliente(cls, cliente_id: str = None, nome: str = None) -> list:
        """
        Selecionando cliente por nome ou id
        :param cliente_id: id do cliente
        :param nome: nome do cliente
        :return: lista de cliente
        """
        try:
            query_data = None
            if cliente_id and not nome:
                with DBConnetionHandler() as db_connection:
                    data = (
                        db_connection.session.query(clienteModel)
                        .filter_by(id=cliente_id)
                        .one()
                    )
                    query_data = [data]
            elif not cliente_id and nome:
                with DBConnetionHandler() as db_connection:
                    data = (
                        db_connection.session.query(clienteModel)
                        .filter_by(nome=nome)
                        .one()
                    )
                    query_data = [data]
            elif cliente_id and nome:
                with DBConnetionHandler() as db_connection:
                    data = (
                        db_connection.session.query(clienteModel)
                        .filter_by(id=cliente_id, nome=nome)
                        .one()
                    )
                    query_data = [data]
            return query_data
        except:
            db_connection.session.rollback()
            raise
        finally:
            db_connection.session.close()

    @classmethod
    def register_cliente(cls, nome: str, email: str) -> Dict[bool, Clientes]:
        """ Registrando um cliente """
        response = None
        validate_entry = isinstance(nome, str) and isinstance(email, str)
        if validate_entry:
            response  = cls.insert_cliente(nome, email)

        return { "Sucess": validate_entry, "Data": response }

    @classmethod
    def encontar_cliente(cls, id: str) -> Dict[bool, Clientes]:
        """ Encontrando um cliente """
        response = None
        validate_entry = isinstance(id, str)
        if validate_entry:
            response = cls.encontar_cliente(id)

        return { "Sucess": validate_entry, "Data": response }