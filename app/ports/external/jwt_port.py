from abc import ABC, abstractmethod

from app.core.collections import Auth, Token
from app.core.helpers.constants import NOT_IMPLEMENTED_ERROR


class JwtPort(ABC):

    @abstractmethod
    def encode_bearer(self, auth: Auth, ispb: str, key: str) -> str:
        raise NotImplementedError(NOT_IMPLEMENTED_ERROR)

    @abstractmethod
    def decode_bearer(self, bearer: str, key: str) -> Token:
        raise NotImplementedError(NOT_IMPLEMENTED_ERROR)
