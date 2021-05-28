from faker import Faker
from src.infra.config import DBConnetionHandler
from .cliente_repository import ClienteRepository

faker = Faker()
clienteRepository = ClienteRepository()
db_connection_handler = DBConnetionHandler()


def test_insert_cliente():
    """Testando o insert cliente"""
    nome = faker.name()
    email = faker.email()
    engine = db_connection_handler.get_engine()

    # SQL
    cliente = clienteRepository.insert_cliente(nome, email)
    query_cliente = engine.execute(
        f"SELECT * FROM clientes WHERE id='{cliente.id}'"
    ).fetchone()
    engine.execute(f"DELETE FROM clientes WHERE id='{cliente.id}'")

    assert cliente.id == query_cliente.id
    assert cliente.nome == query_cliente.nome
    assert cliente.email == query_cliente.email
