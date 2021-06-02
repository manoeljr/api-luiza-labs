class HttpErrors:
    """ Class de definição dos Erros """

    @staticmethod
    def error_422():
        """ HTTP 422 """

        return {"status_code": 422, "body": {"error": "Erro no processamento"}}

    @staticmethod
    def error_400():
        """ HTTP 400 """

        return {"status_code": 400, "body": {"error": "Página não encontrada"}}