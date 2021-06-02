from src.domain.models import Produtos
from src.infra.entities import Produtos as ProdutoModel
from src.data.interfaces import ProdutoRepositoryInterfaces
from src.infra.config import DBConnetionHandler


class ProdutoRepository(ProdutoRepositoryInterfaces):
    """Produto repository"""

    @classmethod
    def inserir_produto(
        cls, preco: float, imagem: str, nome_produto: str, titulo: str, cliente_id: str
    ) -> Produtos:
        """
        Inserindo um produto favorito
        :param - preco
        :param - imagem
        :param - nome_produto
        :param - titulo
        :param - cliente_id
        :return - Produto
        """
        with DBConnetionHandler() as db_connection:
            try:
                produto = ProdutoModel(
                    preco=preco,
                    imagem=imagem,
                    nome_produto=nome_produto,
                    titulo=titulo,
                    cliente_id=cliente_id,
                )
                db_connection.session.add(produto)
                db_connection.session.commit()
                return Produtos(
                    id=produto.id,
                    preco=produto.preco,
                    imagem=produto.imagem,
                    nome_produto=produto.nome_produto,
                    titulo=produto.titulo,
                    cliente_id=produto.cliente_id,
                )
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()

    @classmethod
    def selecionar_produtos(
        cls, produto_id: str = None, cliente_id: str = None
    ) -> list[Produtos]:
        """
        Selecionando um produto
        :param - produto_id
        :param - cliente_id
        :return lista de produtos selecionados
        """
        try:
            query_data = None
            if produto_id and not cliente_id:
                with DBConnetionHandler() as db_connection:
                    data = (
                        db_connection.session.query(ProdutoModel)
                        .filter_by(id=produto_id)
                        .one()
                    )
                    query_data = [data]
            elif not produto_id and cliente_id:
                with DBConnetionHandler() as db_connection:
                    data = (
                        db_connection.session.query(ProdutoModel)
                        .filter_by(cliente_id=cliente_id)
                        .all()
                    )
                    query_data = data
            elif produto_id and cliente_id:
                with DBConnetionHandler() as db_connection:
                    data = (
                        db_connection.session.query(ProdutoModel)
                        .filter_by(id=produto_id, cliente_id=cliente_id)
                        .one()
                    )
                    query_data = [data]
            return query_data
        except:
            db_connection.session.rollback()
            raise
        finally:
            db_connection.session.close()

    @classmethod
    def buscar_produto(cls, id: str, produto_id: str) -> list[Produtos]:
        pass

    @classmethod
    def deletar_produto(cls, id: str):
        pass