
from abc import abstractmethod
from typing import Optional

from app.core.constants import NOT_IMPLEMENTED_ERROR
# from app.core.collections import Account
from app.core.helpers.http import HttpResponse

from .usecase import InputData, Usecase


class SendPixParams(InputData):
    amount: int
    description: str
    from_account: str
    to_account: Optional[str] = None
    to_key: Optional[str] = None
    to_key_key: Optional[str] = None


class SendPixResponse(InputData):
    pass


class SendPixPort(Usecase):
    @abstractmethod
    def execute(self) -> HttpResponse:
        raise NotImplementedError(NOT_IMPLEMENTED_ERROR)
