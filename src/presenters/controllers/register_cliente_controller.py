from typing import Type
from src.domain.use_cases.cliente.register_cliente import RegisterCliente
from src.presenters.errors import HttpErrors
from src.presenters.helpers.http_models import HttpRequest, HttpResponse


class RegisterClienteController:
    """Classe de controller Registro de Cliente"""

    def __init__(self, register_cliente_use_case: Type[RegisterCliente]):
        self.register_cliente_use_case = register_cliente_use_case

    def route(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """Metodo de resposta de caso de uso"""
        response = None
        if http_request.body:
            body_param = http_request.body.keys()
            if "nome" in body_param and "email":
                nome = http_request.body["nome"]
                email = http_request.body["email"]
                response = self.register_cliente_use_case.register(
                    nome=nome, email=email
                )
            else:
                response = {"Sucess": False, "Data": None}
        else:
            response = {"Sucess": False, "Data": None}

        if response["Sucess"] is False:
            http_error = HttpErrors.error_422()
            return HttpResponse(
                status_code=http_error["status_code"], body=http_error["body"]
            )

        return HttpResponse(status_code=200, body=response["Data"])

        http_error = HttpErrors.error_400()
        return HttpResponse(
            status_code=http_error["status_code"], body=http_error["body"]
        )
