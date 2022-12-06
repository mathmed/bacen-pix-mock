from http import HTTPStatus
from traceback import format_exc

from app.core.collections import Key
from app.core.constants import ERROR_TO_SAVE_MESSAGE
from app.core.helpers.http import HttpError, HttpResponse, HttpStatus
from app.core.helpers.token.token import get_token
from app.ports.external import DatabasePort
from app.ports.usecases import (CreateKeyParams, CreateKeyPort,
                                CreateKeyResponse)


class CreateKey(CreateKeyPort):

    def __init__(self, params: CreateKeyParams, database: DatabasePort) -> None:
        self.params = params
        self.database = database

    def execute(self) -> HttpResponse:
        dto = self._validate_params()
        self._verify_if_ispb_exists()
        self._verify_if_key_exists()
        id = self._save_key(dto)
        return HttpStatus.created_201(CreateKeyResponse(id=id))

    def _save_key(self, dto: Key) -> str:
        try:
            return self.database.save(dto)
        except Exception:
            print(format_exc())
            raise HttpError(HTTPStatus.BAD_REQUEST,
                            ERROR_TO_SAVE_MESSAGE)

    def _verify_if_key_exists(self):

        keys = self.database.get_by_filters(
            'Key', [{'keyValue': self.params.key}])
        if len(keys) > 0:
            raise HttpError(HTTPStatus.CONFLICT,
                            f'Key {self.params.key} already exists')

    def _verify_if_ispb_exists(self):
        ispb = get_token().ispb
        institutions = self.database.get_by_filters(
            'Institution', [{'ispb': ispb}])
        if len(institutions) == 0:
            raise HttpError(HTTPStatus.NOT_FOUND,
                            f'Ispb {ispb} not exists')

    def _validate_params(self) -> Key:
        try:
            ispb = get_token().ispb
            return Key(
                account_number=self.params.account.account_number,
                account_type=self.params.account.account_type,
                branch=self.params.account.branch,
                ispb=ispb,
                key_type=self.params.key_type,
                key_value=self.params.key,
                owner_document=self.params.owner.document,
                owner_name=self.params.owner.name
            )
        except AssertionError as e:
            print(format_exc())
            raise HttpError(HTTPStatus.UNPROCESSABLE_ENTITY, str(e))
