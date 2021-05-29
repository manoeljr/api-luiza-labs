from abc import ABC, abstractmethod
from typing import List
from src.domain.models import Clientes


class ClienteRepositoryInterfaces(ABC):
    """Interface de ClienteRepository"""

    @abstractmethod
    def insert_cliente(self, nome: str, email: str) -> Clientes:
        """Metodo abstrato"""
        raise Exception("Metodo não implementado")

    @abstractmethod
    def select_cliente(self, nome: str = None, email: str = None) -> List[Clientes]:
        """Metodo abstrato"""
        raise Exception("Metodo não implementado")
