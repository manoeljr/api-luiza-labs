import uuid
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, String, ForeignKey, Float
from src.infra.config import Base


class Produtos(Base):
    """ Entidade Produtos """

    __tablename__ = "produtos"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4())
    preco = Column(Float, nullable=False)
    imagem = Column(String)
    nome_produto = Column(String, nullable=False, unique=True)
    titulo = Column(String)
    cliente_id = Column(UUID(as_uuid=True), ForeignKey("clientes.id"))

    def __repr__(self):
        return f"Produto: [nome={self.nome_produto}, titulo: {self.titulo}, preco: {self.preco}, imagem: {self.imagem}, imagem: {self.imagem}]"
