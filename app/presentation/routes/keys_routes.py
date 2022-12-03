from http import HTTPStatus

from fastapi import Request, Response

from app.adapters.fastapi_adapter import fastapi_adapter
from app.main import app
from app.ports.usecases.create_key_port import CreateKeyParams
from app.ports.usecases.get_key_port import GetKeyParams
from app.presentation.factories import create_key_factory, get_key_factory

TAGS = ['Chaves']
PREFIX = '/keys'


@app.post(
    PREFIX,
    status_code=HTTPStatus.OK,
    summary='Criar chave PIX',
    responses={},
    tags=TAGS
)
def create_key(request: Request, response: Response, body: CreateKeyParams):
    return fastapi_adapter(response, create_key_factory(body))


@app.get(
    PREFIX,
    status_code=HTTPStatus.OK,
    summary='Buscar chave PIX',
    responses={},
    tags=TAGS
)
def get_key(request: Request, response: Response):
    return fastapi_adapter(response, get_key_factory(GetKeyParams()))
