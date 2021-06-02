from abc import ABC, abstractmethod
from typing import Dict
from src.domain.models import Produtos


class RegisterProduto(ABC):
    """ Interface de Produto """

    @abstractmethod
    def register(cls, preco: float, imagem: str, nome_produto: str, titulo: str, cliente_id: str) -> Dict[bool, Produtos]:
        """ Metodo abstrato registrar produto """

        raise Exception("Implementação do metodo RegisterProduto")