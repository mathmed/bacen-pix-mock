from http import HTTPStatus
from typing import List

from app.core.collections import Key
from app.core.helpers.http import HttpError, HttpResponse, HttpStatus
from app.ports.external import DatabasePort
from app.ports.usecases import GetKeyParams, GetKeyPort, GetKeyResponse


class GetKey(GetKeyPort):

    def __init__(self, params: GetKeyParams, database: DatabasePort) -> None:
        self.params = params
        self.database = database

    def execute(self) -> HttpResponse:
        key = self._get_key()
        return HttpStatus.ok_200(GetKeyResponse(**key.to_dict()))

    def _get_key(self) -> Key:
        key: List[Key] = self.database.get_by_filters(
            'Key', [{'keyValue': self.params.key}])
        if len(key) == 0:
            raise HttpError(HTTPStatus.NOT_FOUND,
                            f'Key {self.params.key} not found')
        return key[0]
