
from abc import abstractmethod

from app.core.helpers.constants import NOT_IMPLEMENTED_ERROR
from app.core.helpers.http import HttpResponse

from .usecase import InputData, Usecase


class GetKeyResponse(InputData):
    key_type: str
    key_value: str
    owner_document: str
    owner_name: str
    ispb: str
    branch: str
    account_number: str
    account_type: str


class GetKeyParams(InputData):
    key: str


class GetKeyPort(Usecase):
    @abstractmethod
    def execute(self) -> HttpResponse:
        raise NotImplementedError(NOT_IMPLEMENTED_ERROR)
