
from abc import abstractmethod

from app.core.helpers.constants import NOT_IMPLEMENTED_ERROR
from app.core.helpers.http import HttpResponse

from .usecase import InputData, Usecase


class CreateInstitutionParams(InputData):
    name: str
    ispb: str
    document: str
    callback_url: str
    basic_user: str
    basic_password: str


class CreateInstitutionResponse(InputData):
    id: str


class CreateInstitutionPort(Usecase):
    @abstractmethod
    def execute(self) -> HttpResponse:
        raise NotImplementedError(NOT_IMPLEMENTED_ERROR)
