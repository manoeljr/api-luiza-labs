from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DBConnetionHandler:
    """  Conexao base de dados com Sqlalchemy  """

    def __init__(self):
        self.__connection_string = (
            "postgresql+psycopg2://postgres:docker@127.0.0.1:5432/luizalabs"
        )
        self.session = None

    def get_engine(self):
        """
        Return Conexao Engine
        :param None
        :return Conexao da base de dados, engine
        """
        engine = create_engine(self.__connection_string)
        return engine

    def __enter__(self):
        """
        Return Sessao da conexao
        :param None
        :return session
        """
        engine = create_engine(self.__connection_string)
        session_maker = sessionmaker()
        self.session = session_maker(bind=engine)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Return None
        :param exc_type:
        :param exc_val:
        :param exc_tb:
        :return:
        """
        self.session.close()
