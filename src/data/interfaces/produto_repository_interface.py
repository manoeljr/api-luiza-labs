from abc import ABC, abstractmethod
from typing import List
from src.domain.models import Produtos


class ProdutoRepositoryInterfaces(ABC):
    """Interface de ClienteRepository"""

    @abstractmethod
    def insert_produto(
        self,
        preco: float,
        imagem: str,
        nome_produto: str,
        titulo: str,
        cliente_id: str,
    ) -> Produtos:
        """Metodo abstrato"""
        raise Exception("Metodo não implementado")

    @abstractmethod
    def select_produto(
        self,
        id: str = None,
        preco: float = None,
        imagem: str = None,
        nome_produto: str = None,
        titulo: str = None,
        cliente_id: str = None,
    ) -> List[Produtos]:
        """Metodo abstrato"""
        raise Exception("Metodo não implementado")
