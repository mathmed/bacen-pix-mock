from http import HTTPStatus

from fastapi import Depends, Header, Response
from fastapi.security import HTTPBasic, HTTPBasicCredentials

from app.adapters.http import fastapi_adapter
from app.core.helpers.http import HandledError
from app.main import app
from app.ports.usecases.auth_port import AuthParams, AuthResponse
from app.presentation.factories import auth_factory

TAGS = ['Autenticação']
PREFIX = '/signin'

security_basic = HTTPBasic(auto_error=False)


@app.post(
    f'{PREFIX}',
    status_code=HTTPStatus.OK,
    summary='Realiza autenticação no serviço',
    responses={
        HTTPStatus.OK.value: {
            'model': AuthResponse
        },
        HTTPStatus.UNAUTHORIZED.value: {
            'model': HandledError
        }
    },
    tags=TAGS
)
def auth(response: Response, ispb: str = Header(), credentials: HTTPBasicCredentials = Depends(security_basic)):
    params = AuthParams(
        ispb=ispb,
        password=credentials.password,
        user=credentials.username
    )
    return fastapi_adapter(response, auth_factory(params))
