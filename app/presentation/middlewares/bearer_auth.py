

from functools import wraps
from http import HTTPStatus
from time import time
from traceback import format_exc
from typing import Dict, Optional

from app.adapters.database import MongoDBAdapter
from app.adapters.jwt import JwtAdapter
from app.core.collections import Auth, Control, Token
from app.core.constants import (ERROR_TO_AUTHENTICATE_MESSAGE,
                                INVALID_AUTH_METHOD_MESSAGE,
                                INVALID_BEARER_MESSAGE,
                                INVALID_USER_PASS_OR_ISPB_MESSAGE,
                                TOKEN_EXPIRED_MESSAGE)
from app.core.helpers.http import HttpError
from app.core.helpers.http.http import HandledError
from app.core.helpers.token import set_token


def bearer_auth_middleware(func):
    @wraps(func)
    def wrapper(*args, **kwargs):

        request = kwargs.get('request', None)
        response: object = kwargs.get('response', None)

        try:

            headers: Dict = getattr(request, 'headers', {})

            auth_header: Optional[str] = headers.get('Authorization', None)

            if not auth_header:
                raise HttpError(HTTPStatus.FORBIDDEN,
                                INVALID_AUTH_METHOD_MESSAGE)

            auth_type, bearer = auth_header.split(' ')

            if auth_type.lower() != 'bearer':
                raise HttpError(HTTPStatus.FORBIDDEN,
                                INVALID_AUTH_METHOD_MESSAGE)

            _validate_bearer(bearer)

            return func(*args, **kwargs)

        except HttpError as e:
            response.status_code = e.status_code
            return HandledError(message=e.message)

        except Exception:
            response.status_code = HTTPStatus.FORBIDDEN
            return HandledError(message=ERROR_TO_AUTHENTICATE_MESSAGE)

    return wrapper


def _validate_bearer(bearer: str):
    token = _read_bearer(bearer)
    user_id = _verify_user(token)
    _verify_bearer(token, user_id)
    set_token(token)


def _read_bearer(bearer: str) -> Token:
    try:
        jwt = JwtAdapter()
        return jwt.decode_bearer(bearer, _get_jwt_key())
    except Exception:
        print(format_exc())
        raise HttpError(HTTPStatus.UNAUTHORIZED, INVALID_BEARER_MESSAGE)


def _get_jwt_key() -> str:
    try:
        mongo = MongoDBAdapter()
        filters = [{'key': 'jwt_key'}]
        control: Control = mongo.get_by_filters('Control', filters)[
            0]
        return control.value
    except Exception:
        print(format_exc())
        raise HttpError(HTTPStatus.UNAUTHORIZED,
                        ERROR_TO_AUTHENTICATE_MESSAGE)


def _verify_user(token: Token) -> str:
    try:
        mongo = MongoDBAdapter()
        filters = [{'_id': token.user_id}]
        user: Auth = mongo.get_by_filters('Auth', filters)[
            0]
        return user.id
    except Exception:
        print(format_exc())
        raise HttpError(HTTPStatus.FORBIDDEN,
                        INVALID_USER_PASS_OR_ISPB_MESSAGE)


def _verify_bearer(token: Token, user_id: str):
    try:
        if token.user_id != user_id:
            raise HttpError(HTTPStatus.FORBIDDEN,
                            INVALID_USER_PASS_OR_ISPB_MESSAGE)

        if token.exp < int(time()):
            raise HttpError(HTTPStatus.FORBIDDEN,
                            TOKEN_EXPIRED_MESSAGE)

    except Exception:
        print(format_exc())
        raise HttpError(HTTPStatus.FORBIDDEN,
                        INVALID_USER_PASS_OR_ISPB_MESSAGE)
