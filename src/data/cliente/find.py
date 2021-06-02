from src.domain.use_cases import FindCliente as FindClienteInterface
from typing import Type, Dict, List
from src.domain.models import Clientes
from src.data.interfaces import ClienteRepositoryInterfaces as ClienteRepository


class FindCliente(FindClienteInterface):
    """ Classe definição do caso de uso  FindCliente """

    def __init__(self, clienteRepository: Type[ClienteRepository]):
        self.clienteRepository = ClienteRepository

    def by_id(cls, cliente_id: str) -> Dict[bool, List[Clientes]]:
        """
        Selecionando o cliente por ID
        :param - ID
        :return - Dicionario
        """
        response = None
        validate_entry = isinstance(cliente_id, str)

        if validate_entry:
            response = cls.clienteRepository.selecionar_clientes(cliente_id=cliente_id)

        return {"Sucess": validate_entry, "Data": response}

    def by_nome(cls, nome: str) -> Dict[bool, List[Clientes]]:
        """
        Selecionando o cliente por NOME
        :param - NOME
        :return - Dicionario
        """
        response = None
        validate_entry = isinstance(nome, str)

        if validate_entry:
            response = cls.clienteRepository.selecionar_clientes(nome=nome)

        return {"Sucess": validate_entry, "Data": response}

    def by_email(cls, email: str) -> Dict[bool, List[Clientes]]:
        """
        Selecionando o cliente por EMAIL
        :param - EMAIL
        :return - Dicionario
        """
        response = None
        validate_entry = isinstance(email, str)

        if validate_entry:
            response = cls.clienteRepository.selecionar_clientes(email=email)

        return {"Sucess": validate_entry, "Data": response}

