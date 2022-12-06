
from abc import abstractmethod

from app.core.constants import NOT_IMPLEMENTED_ERROR
from app.core.helpers.http import HttpResponse

from .usecase import InputData, Usecase


class DeletetKeyParams(InputData):
    key: str


class DeleteKeyPort(Usecase):
    @abstractmethod
    def execute(self) -> HttpResponse:
        raise NotImplementedError(NOT_IMPLEMENTED_ERROR)
