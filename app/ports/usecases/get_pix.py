
from abc import abstractmethod

from app.core.helpers.http import HttpResponse

from .usecase import NOT_IMPLEMENTED_ERROR, InputData, Usecase


class GetPixParams(InputData):
    pass


class GetPixResponse(InputData):
    pass


class GetPixPort(Usecase):
    @abstractmethod
    def execute(self) -> HttpResponse:
        raise NotImplementedError(NOT_IMPLEMENTED_ERROR)
