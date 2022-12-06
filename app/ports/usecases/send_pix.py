
from abc import abstractmethod
from typing import Optional

from app.core.helpers.constants import NOT_IMPLEMENTED_ERROR
from app.core.helpers.enums import AccountTypes, KeyTypes, PixStatus, PixTypes
from app.core.helpers.http import HttpResponse

from .usecase import InputData, Usecase


class Account(InputData):
    branch: str
    number: str
    type: AccountTypes
    owner_name: str
    owner_document: str


class SendPixParams(InputData):
    amount: int
    description: str
    pix_type: PixTypes
    from_account: Account
    to_account: Optional[Account] = None
    to_key: Optional[str] = None
    to_key_type: Optional[KeyTypes] = None
    to_ispb: str


class SendPixResponse(InputData):
    end2endId: str
    status: PixStatus


class SendPixPort(Usecase):
    @abstractmethod
    def execute(self) -> HttpResponse:
        raise NotImplementedError(NOT_IMPLEMENTED_ERROR)
