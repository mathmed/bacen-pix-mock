from http import HTTPStatus

from fastapi import Request, Response

from app.adapters.fastapi_adapter import fastapi_adapter
from app.main import app
from app.ports.usecases.create_ispb import CreateISPBParams
from app.presentation.factories import create_ispb_factory

TAGS = ['ISPB']
PREFIX = '/ispb'


@app.post(
    PREFIX,
    status_code=HTTPStatus.OK,
    summary='Cadastrar novo ISPB',
    responses={},
    tags=TAGS
)
def create_ispb(request: Request, response: Response, body: CreateISPBParams):
    return fastapi_adapter(response, create_ispb_factory(body))
