
from abc import abstractmethod

from app.core.helpers.constants import NOT_IMPLEMENTED_ERROR
from app.core.helpers.http import HttpResponse

from .usecase import InputData, Usecase


class GetPixParams(InputData):
    pass


class GetPixResponse(InputData):
    pass


class GetPixPort(Usecase):
    @abstractmethod
    def execute(self) -> HttpResponse:
        raise NotImplementedError(NOT_IMPLEMENTED_ERROR)
