# import uuid
# from src.infra.entities import Produtos
# from faker import Faker
# from src.infra.config import DBConnetionHandler
# from src.infra.repositories.produto_repository import ProdutoRepository
#
# faker = Faker()
# produtoRepository = ProdutoRepository()
# db_connection_handler = DBConnetionHandler()
#
#
# def test_insert_produto():
#     """ Testando o insert produto """
#     preco = faker.random_number()
#     imagem = faker.text()
#     nome_produto = faker.name()
#     titulo = faker.name()
#     cliente_id = faker.random.__hash__(uuid.uuid4())
#     engine = db_connection_handler.get_engine()
#
#     # SQL
#     produto = produtoRepository.insert_produto(preco, imagem, nome_produto, titulo, cliente_id)
#     query_produto = engine.execute(
#         f"SELECT * FROM produtos WHERE id='{produto.id}'"
#     ).fetchone()
#     engine.execute(f"DELETE FROM produtos WHERE id='{produto.id}'")
#
#     assert produto.id == query_produto.id
#     assert produto.preco == query_produto.preco
#     assert produto.imagem == query_produto.imagem
#     assert produto.nome_produto == query_produto.nome_produto
#     assert produto.titulo == query_produto.titulo
#     assert produto.cliente_id == query_produto.cliente_id
#
# def test_select_produto():
#     """ Testando select produto """
#     produto_id = faker.random.__hash__(uuid.uuid4())
#     preco = faker.random_number()
#     imagem = faker.text()
#     nome_produto = faker.name()
#     titulo = faker.name()
#     cliente_id = faker.random.__hash__(uuid.uuid4())
#
#     data = Produtos(id = produto_id, preco = preco, imagem = imagem, nome_produto = nome_produto, titulo = titulo, cliente_id = cliente_id)
#
#     engine = db_connection_handler.get_engine()
#     engine.execute(f"INSERT INTO produtos (id, preco, imagem, nome_produto, titulo, cliente_id) VALUES '{produto_id}', '{preco}', '{imagem}', '{imagem}', '{nome_produto}', '{titulo}', '{cliente_id}'")
#
#     query_produto1 = produtoRepository.select_produto(produto_id=produto_id)
#     query_produto2 = produtoRepository.select_produto(cliente_id=cliente_id)
#     query_produto3 = produtoRepository.select_produto(produto_id=produto_id, cliente_id=cliente_id)
#
#     assert data in query_produto1
#     assert data in query_produto2
#     assert data in query_produto3
