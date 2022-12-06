from http import HTTPStatus
from traceback import format_exc
from typing import List

from app.core.collections import Auth as AuthCollection
from app.core.collections import Control, Institution
from app.core.constants import (ERROR_TO_AUTHENTICATE,
                                INVALID_USER_PASS_OR_ISPB, TOKEN_EXPIRES_IN)
from app.core.helpers.http import HttpError, HttpResponse, HttpStatus
from app.ports.external import DatabasePort, EncryptPort, JwtPort
from app.ports.usecases import AuthParams, AuthPort, AuthResponse


class Auth(AuthPort):

    def __init__(self, params: AuthParams, database: DatabasePort, encrypt: EncryptPort, jwt: JwtPort) -> None:
        self.params = params
        self.database = database
        self.encrypt = encrypt
        self.jwt = jwt

    def execute(self) -> HttpResponse:

        user = self._verify_user()
        token = self._make_token(user)
        return HttpStatus.ok_200(AuthResponse(
            access_token=str(token),
            expires_in=TOKEN_EXPIRES_IN
        ))

    def _make_token(self, auth: AuthCollection):
        try:
            return self.jwt.encode_bearer(auth, self.params.ispb, self._get_jwt_key())
        except Exception:
            print(format_exc())
            raise HttpError(HTTPStatus.UNAUTHORIZED,
                            ERROR_TO_AUTHENTICATE)

    def _verify_user(self) -> AuthCollection:
        try:
            filters = [{'user': self.params.user}]
            user: AuthCollection = self.database.get_by_filters('Auth', filters)[
                0]
            if not user or not self.encrypt.verify(user.password, self.params.password) or not self._verify_institution(user):
                raise HttpError(HTTPStatus.UNAUTHORIZED,
                                INVALID_USER_PASS_OR_ISPB)
            return user
        except Exception:
            print(format_exc())
            raise HttpError(HTTPStatus.UNAUTHORIZED,
                            INVALID_USER_PASS_OR_ISPB)

    def _verify_institution(self, user: AuthCollection) -> bool:
        institutions: List[Institution] = self.database.get_by_filters(
            'Institution', [{'_id': user.id}])
        if not institutions or institutions[0].ispb != self.params.ispb:
            return False
        return True

    def _get_jwt_key(self) -> str:
        try:
            filters = [{'key': 'jwt_key'}]
            control: Control = self.database.get_by_filters('Control', filters)[
                0]
            return control.value
        except Exception:
            print(format_exc())
            raise HttpError(HTTPStatus.UNAUTHORIZED,
                            ERROR_TO_AUTHENTICATE)
