# import uuid
#
# from faker import Faker
# from src.infra.config import DBConnetionHandler
# from src.infra.entities import Clientes
# from src.infra.repositories.cliente_repository import ClienteRepository
#
# faker = Faker()
# clienteRepository = ClienteRepository()
# db_connection_handler = DBConnetionHandler()
#
#
# def test_insert_cliente():
#     """Testando o insert cliente"""
#     nome = faker.name()
#     email = faker.email()
#     engine = db_connection_handler.get_engine()
#
#     # SQL
#     cliente = clienteRepository.insert_cliente(nome, email)
#     query_cliente = engine.execute(
#         f"SELECT * FROM clientes WHERE id='{cliente.id}'"
#     ).fetchone()
#     engine.execute(f"DELETE FROM clientes WHERE id='{cliente.id}'")
#
#     assert cliente.id == query_cliente.id
#     assert cliente.nome == query_cliente.nome
#     assert cliente.email == query_cliente.email
#
# def test_select_cliente():
#     """ Testando o Select cliente """
#     cliente_id = faker.random.__hash__(uuid.uuid4())
#     nome = faker.name()
#     email = faker.email()
#     data = Clientes(id = cliente_id, nome = nome, email = email)
#     engine = db_connection_handler.get_engine()
#     engine.execute(f"INSERT INTO clientes (id, nome, email) VALUES ('{cliente_id}','{nome}','{email}')")
#
#     query_cliente1 = clienteRepository.select_cliente(cliente_id=cliente_id)
#     query_cliente2 = clienteRepository.select_cliente(nome=nome)
#     query_cliente3 = clienteRepository.select_cliente(cliente_id=cliente_id, nome=nome)
#
#     assert data in query_cliente1
#     assert data in query_cliente2
#     assert data in query_cliente3
#
#     engine.execute(f"DELETE FROM clientes WHERE id='{cliente_id}'")
