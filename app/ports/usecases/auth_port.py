
from abc import abstractmethod

from app.core.constants import NOT_IMPLEMENTED_ERROR
from app.core.helpers.http import HttpResponse

from .usecase import InputData, Usecase


class AuthResponse(InputData):
    access_token: str
    expires_in: int
    type: str = 'Bearer'


class AuthParams(InputData):
    user: str
    password: str
    ispb: str


class AuthPort(Usecase):
    @abstractmethod
    def execute(self) -> HttpResponse:
        raise NotImplementedError(NOT_IMPLEMENTED_ERROR)
