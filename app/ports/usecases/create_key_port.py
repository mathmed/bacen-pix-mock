
from abc import abstractmethod

from app.core.enums.enums import AccountTypes, KeyTypes
from app.core.helpers.http import HttpResponse

from .usecase import NOT_IMPLEMENTED_ERROR, InputData, Usecase


class Owner(InputData):
    document: str
    name: str


class Account(InputData):
    ispb: str
    branch: str
    account_number: str
    account_type: AccountTypes


class CreateKeyParams(InputData):
    key: str
    key_type: KeyTypes
    owner: Owner
    account: Account


class CreateKeyResponse(InputData):
    id: str


class CreateKeyPort(Usecase):
    @abstractmethod
    def execute(self) -> HttpResponse:
        raise NotImplementedError(NOT_IMPLEMENTED_ERROR)
