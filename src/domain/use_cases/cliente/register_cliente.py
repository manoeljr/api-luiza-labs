from abc import ABC, abstractmethod
from src.domain.models import Clientes
from typing import Dict


class RegisterCliente(ABC):
    """ Interface registro de cliente """

    @abstractmethod
    def register(cls, nome: str, email: str) -> Dict[bool, Clientes]:
        """  Caso de uso da representação do cliente """
        raise Exception("Implementação do metodo Register")
