from typing import Type, Dict
from src.domain.use_cases import RegisterCliente as RegisterClienteInterface
from src.data.interfaces import ClienteRepositoryInterfaces as ClienteRepository
from src.domain.models import Clientes


class RegisterCliente(RegisterClienteInterface):
    """ Classe de implementação do cliente caso de uso """

    def __init__(self, clienteRepository: Type[ClienteRepository]):
        self.clienteRepository = clienteRepository

    def register(self, nome: str, email: str) -> Dict[bool, Clientes]:
        """
        Registro de caso de uso do cliente
        :param - nome, nome do cliente
        :param - email, email do cliente
        :return - retorna um dicionario
        """
        response = None
        validate_entry = isinstance(nome, str) and isinstance(email, str)

        if validate_entry:
            response = self.clienteRepository.inserir_cliente(nome, email)
        return { "Sucess": validate_entry, "Data": response }
