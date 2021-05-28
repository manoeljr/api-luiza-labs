import uuid
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from src.infra.config import Base


class Clientes(Base):
    """Entidade Cliente"""

    __tablename__ = "clientes"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4())
    nome = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    # Definindo o Nome do relacionamento com a tabela de produtos favoritos
    id_produto = relationship("Produtos")

    def __repr__(self):
        return f"Cliente [nome={self.nome}]"

    def __eq__(self, other):
        if (
            self.id == other.id
            and self.nome == other.nome
            and self.email == other.email
        ):
            return True
        return False
