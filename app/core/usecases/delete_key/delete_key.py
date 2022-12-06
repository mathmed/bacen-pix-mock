from http import HTTPStatus
from traceback import format_exc
from typing import List

from app.core.collections import Key
from app.core.helpers.http import HttpError, HttpResponse, HttpStatus
from app.core.helpers.token import get_token
from app.ports.external import DatabasePort
from app.ports.usecases import DeleteKeyPort, DeletetKeyParams


class DeleteKey(DeleteKeyPort):

    def __init__(self, params: DeletetKeyParams, database: DatabasePort) -> None:
        self.params = params
        self.database = database

    def execute(self) -> HttpResponse:
        key = self._get_key()
        self._verify_ispb(key.ispb)
        self._delete_key(key.id)
        return HttpStatus.no_content_204()

    def _get_key(self) -> Key:
        key: List[Key] = self.database.get_by_filters(
            'Key', [{'keyValue': self.params.key}])
        if len(key) == 0:
            raise HttpError(HTTPStatus.NOT_FOUND,
                            f'Key {self.params.key} not found')
        return key[0]

    def _verify_ispb(self, key_ispb: str):
        if key_ispb != get_token().ispb:
            raise HttpError(HTTPStatus.FORBIDDEN,
                            f'Cannot delete Key')

    def _delete_key(self, id: str):
        try:
            self.database.delete(
                id=id,
                collection=Key.__name__
            )
        except Exception:
            print(format_exc())
            raise HttpError(HTTPStatus.BAD_REQUEST,
                            f'Error to delete Key {self.params.key}')
