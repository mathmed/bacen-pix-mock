
from abc import abstractmethod

from app.core.collections import Key
from app.core.helpers.http import HttpResponse

from .usecase import NOT_IMPLEMENTED_ERROR, InputData, Usecase


class GetKeyParams(InputData):
    key: str


class GetKeyResponse(Key):
    pass


class GetKeyPort(Usecase):
    @abstractmethod
    def execute(self) -> HttpResponse:
        raise NotImplementedError(NOT_IMPLEMENTED_ERROR)
