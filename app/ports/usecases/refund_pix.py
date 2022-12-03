
from abc import abstractmethod

from app.core.helpers.http import HttpResponse

from .usecase import NOT_IMPLEMENTED_ERROR, InputData, Usecase


class RefundPixParams(InputData):
    pass


class RefundPixResponse(InputData):
    pass


class RefundPixPort(Usecase):
    @abstractmethod
    def execute(self) -> HttpResponse:
        raise NotImplementedError(NOT_IMPLEMENTED_ERROR)
