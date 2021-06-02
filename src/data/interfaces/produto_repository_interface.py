from abc import ABC, abstractmethod
from typing import List
from src.domain.models import Produtos


class ProdutoRepositoryInterfaces(ABC):
    """Interface de ClienteRepository"""

    @abstractmethod
    def inserir_produto(
        self,
        preco: float,
        imagem: str,
        nome_produto: str,
        titulo: str,
        cliente_id: str,
    ) -> Produtos:
        """ Metodo abstrato de inserir um produto """
        raise Exception("Metodo de cadastro de produto não implementado")

    @abstractmethod
    def selecionar_produtos(self, id_cliente: str) -> List[Produtos]:
        """ Metodo abstrato de selecionar todos produtos """
        raise Exception("Metodo seleção de produto não implementado")

    @abstractmethod
    def buscar_produto(self, id:str, produto_id: str) -> Produtos:
        """ Metode abstrato de buscar um produto """
        pass

    @abstractmethod
    def deletar_produto(self, ):
        """ Metode abstrato de deletar um produto """
        raise Exception("Metodo de registro de produto não implementado ")
