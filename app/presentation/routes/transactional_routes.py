from http import HTTPStatus

from fastapi import Request, Response

from app.adapters.http import fastapi_adapter
from app.main import app
from app.ports.usecases.confirm_pix import ConfirmPixParams
from app.ports.usecases.get_pix import GetPixParams
from app.ports.usecases.refund_pix import RefundPixParams
from app.ports.usecases.send_pix import SendPixParams
from app.presentation.factories import (confirm_pix_factory, get_key_factory,
                                        refund_pix_factory, send_pix_factory)
from app.presentation.factories.get_pix_factory import get_pix_factory

TAGS = ['Transacional']
PREFIX = '/pix'


@app.post(
    f'{PREFIX}',
    status_code=HTTPStatus.OK,
    summary='Enviar PIX (PACS.008)',
    responses={},
    tags=TAGS
)
def send_pix(request: Request, response: Response, body: SendPixParams):
    return fastapi_adapter(response, send_pix_factory(body))


@app.post(
    PREFIX + '/{endToEndId}/refund',
    status_code=HTTPStatus.OK,
    summary='Devolver PIX (PACS.004)',
    responses={},
    tags=TAGS
)
def refund_pix(request: Request, response: Response, body: RefundPixParams, endToEndId: str):
    return fastapi_adapter(response, refund_pix_factory(body))


@app.post(
    PREFIX + '/{endToEndId}/confirm',
    status_code=HTTPStatus.OK,
    summary='Confirmar PIX (PACS.002)',
    responses={},
    tags=TAGS
)
def confirm_pix(request: Request, response: Response, body: ConfirmPixParams, endToEndId: str):
    return fastapi_adapter(response, confirm_pix_factory(body))


@app.get(
    PREFIX + '/{endToEndId}',
    status_code=HTTPStatus.OK,
    summary='Buscar detalhes do PIX',
    responses={},
    tags=TAGS
)
def get_pix(request: Request, response: Response, endToEndId: str):
    return fastapi_adapter(response, get_pix_factory(GetPixParams()))
