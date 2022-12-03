
from abc import abstractmethod

from app.core.helpers.http import HttpResponse

from .usecase import NOT_IMPLEMENTED_ERROR, InputData, Usecase


class ConfirmPixParams(InputData):
    pass


class ConfirmPixResponse(InputData):
    pass


class ConfirmPixPort(Usecase):
    @abstractmethod
    def execute(self) -> HttpResponse:
        raise NotImplementedError(NOT_IMPLEMENTED_ERROR)
