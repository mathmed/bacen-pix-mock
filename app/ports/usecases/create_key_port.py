
from abc import abstractmethod

from app.core.helpers.constants import NOT_IMPLEMENTED_ERROR
from app.core.helpers.enums.enums import AccountTypes, KeyTypes
from app.core.helpers.http import HttpResponse

from .usecase import InputData, Usecase


class Owner(InputData):
    document: str
    name: str


class Account(InputData):
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
