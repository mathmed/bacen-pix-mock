from http import HTTPStatus

from fastapi import Request, Response

from app.adapters.http import fastapi_adapter
from app.core.helpers.http import HandledError
from app.main import app
from app.ports.usecases.create_key_port import (CreateKeyParams,
                                                CreateKeyResponse)
from app.ports.usecases.delete_key_port import DeleteKeyPort, DeletetKeyParams
from app.ports.usecases.get_key_port import GetKeyParams
from app.presentation.factories import (create_key_factory, delete_key_factory,
                                        get_key_factory)
from app.presentation.middlewares import bearer_auth_middleware

TAGS = ['Chaves']
PREFIX = '/keys'


@app.post(
    PREFIX,
    status_code=HTTPStatus.CREATED,
    summary='Criar chave PIX',
    responses={
        HTTPStatus.CREATED.value: {
            'model': CreateKeyResponse
        },
        HTTPStatus.BAD_REQUEST.value: {
            'model': HandledError
        },
        HTTPStatus.NOT_FOUND.value: {
            'model': HandledError
        },
        HTTPStatus.CONFLICT.value: {
            'model': HandledError
        }
    },
    tags=TAGS
)
@bearer_auth_middleware
def create_key(request: Request, response: Response, body: CreateKeyParams):
    return fastapi_adapter(response, create_key_factory(body))


@app.get(
    PREFIX + '/{key}',
    status_code=HTTPStatus.OK,
    summary='Buscar chave PIX',
    responses={
        HTTPStatus.OK.value: {
            'model': HandledError
        },
        HTTPStatus.NOT_FOUND.value: {
            'model': HandledError
        },
    },
    tags=TAGS
)
def get_key(key: str, response: Response):
    return fastapi_adapter(response, get_key_factory(GetKeyParams(key=key)))


@app.delete(
    PREFIX + '/{key}',
    status_code=HTTPStatus.NO_CONTENT,
    summary='Deletar chave PIX',
    responses={
        HTTPStatus.BAD_REQUEST.value: {
            'model': HandledError
        },
        HTTPStatus.NOT_FOUND.value: {
            'model': HandledError
        },
    },
    tags=TAGS
)
def delete_key(key: str, response: Response):
    return fastapi_adapter(response, delete_key_factory(DeletetKeyParams(key=key)))
