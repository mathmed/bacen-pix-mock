
from abc import abstractmethod

from app.core.helpers.http import HttpResponse

from .usecase import NOT_IMPLEMENTED_ERROR, InputData, Usecase


class CreateKeyParams(InputData):
    pass


class CreateKeyResponse(InputData):
    pass


class CreateKeyPort(Usecase):
    @abstractmethod
    def execute(self) -> HttpResponse:
        raise NotImplementedError(NOT_IMPLEMENTED_ERROR)
