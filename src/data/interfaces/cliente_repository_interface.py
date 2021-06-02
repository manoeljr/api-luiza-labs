from abc import ABC, abstractmethod
from typing import List
from src.domain.models import Clientes


class ClienteRepositoryInterfaces(ABC):
    """ Interface de ClienteRepository """

    @abstractmethod
    def inserir_cliente(self, nome: str, email: str) -> Clientes:
        """ Metodo abstrato de inserir um cliente """
        raise Exception("Metodo cadastrar cliente não implementado")

    @abstractmethod
    def selecionar_clientes(self) -> List[Clientes]:
        """ Metodo abstrato de selecionar todos clientes """
        raise Exception("Metodo Selecionar clientes não implementado")

    @abstractmethod
    def deletar_cliente(self, id: str):
        """ Metodo abstrato de deletar um cliente """
        raise Exception("Metodo deletar cliente não implementado")

    @abstractmethod
    def buscar_cliente(self, id: str) -> Clientes:
        """ Metodo abstrato de encontrar um cliente """
        raise Exception("Metodo encontrar clientes não implementado")