from abc import ABC, abstractmethod
from typing import List
from src.domain.models import Clientes


class ClienteRepositoryInterfaces(ABC):
    """ Interface de ClienteRepository """

    @abstractmethod
    def insert_cliente(self, nome: str, email: str) -> Clientes:
        """ Metodo abstrato de inserir um cliente """
        raise Exception("Metodo não implementado")

    @abstractmethod
    def select_cliente(self, nome: str = None, email: str = None) -> List[Clientes]:
        """ Metodo abstrato de selecionar um cliente """
        raise Exception("Metodo não implementado")

    @abstractmethod
    def registrar_cliente(self, nome: str, email: str) -> Clientes:
        """ Metodo de registro de cliente """
        raise Exception("Metodo de registro de cliente")
