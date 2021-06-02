from typing import  Type, Dict
from src.domain.models.produtos import Produtos
from src.data.cliente.find import FindCliente
from src.data.interfaces import ProdutoRepositoryInterfaces as ProdutoRepository
from src.domain.use_cases.produto.register_produto import RegisterProduto as RegisterProdutoInterface



class RegisterProduto(RegisterProdutoInterface):
    """ Classe de interface de produto """

    def __init__(self, produtoRepository: [ProdutoRepository], findCliente: Type[FindCliente]):
        self.produtoRepository = produtoRepository
        self.findCliente = findCliente

    def register(self, preco: float, imagem: str, nome_produto: str, titulo: str, cliente_id: str) -> Dict[bool, Produtos]:
        """ Registrando um produto """
        response = None
        validate_entry = isinstance(preco, float) and isinstance(imagem, str) and isinstance(nome_produto, str) and isinstance(titulo, str) and isinstance(cliente_id, str)
        if validate_entry:
            response = self.register(preco, imagem, nome_produto, titulo, cliente_id)

        return {"Sucess": validate_entry, "Data": response}


