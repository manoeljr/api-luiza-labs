from typing import Type
from src.domain.use_cases.cliente.find_cliente import FindCliente
from src.presenters.helpers import HttpRequest, HttpResponse
from src.presenters.errors.Http_errors import HttpErrors


class FindClienteController:
    """ Controller de Cliente """

    def __int__(self, find_cliente: Type[FindCliente]):
        self.find_cliente = find_cliente

    def handler(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """ Metodo de requisição """

        response = None
        if http_request.query:
            query_string_params = http_request.query.keys()
            if "cliente_id" in query_string_params and "cliente_name" in query_string_params:
                cliente_id = http_request.param['cliente_id']
                response = self.find_cliente.by_id(cliente_id=cliente_id)
            elif ('email' in query_string_params):
                cliente_email = http_request.param['email']
                response = self.find_cliente.by_email(cliente_email)
            else:
                response = {"Success": False, "Data": None}

            if response["Sucess"] is False:
                http_error = HttpErrors.error_422()
                return HttpResponse(status_code=http_error["status_code"], body=http_error["body"])

            return HttpResponse(status_code=200, body=response["Data"])
        http_error = HttpErrors.error_400()
        return HttpResponse(status_code=http_error["status_code"], body=http_error["body"])