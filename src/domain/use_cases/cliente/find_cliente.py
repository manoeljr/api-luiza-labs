from abc import ABC, abstractmethod
from typing import List, Dict
from src.domain.models import Clientes

class FindCliente(ABC):
    """ Interface buscar cliente """

    @abstractmethod
    def by_id(cls, cliente_id: str) -> Dict[bool, List[Clientes]]:
        """ Metodo de busca por ID """
        raise Exception("Implementação do metodo BY_ID")

    @abstractmethod
    def by_nome(cls, nome: str) -> Dict[bool, List[Clientes]]:
        """ Metodo de busca por NOME """
        raise Exception("Implementação do metodo BY_NOME")

    @abstractmethod
    def by_email(cls, email: str) -> Dict[bool, List[Clientes]]:
        """ Metodo de busca por EMAIL """
        raise Exception("Implementação do metodo BY_EMAIL")