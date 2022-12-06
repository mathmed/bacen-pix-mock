from abc import ABC, abstractmethod

from app.core.collections import Auth, Token

METHOD_NOT_IMPLEMENTED = 'Method not implemented'


class JwtPort(ABC):

    @abstractmethod
    def encode_bearer(self, auth: Auth, ispb: str, key: str) -> str:
        raise NotImplementedError(METHOD_NOT_IMPLEMENTED)

    @abstractmethod
    def decode_bearer(self, bearer: str, key: str) -> Token:
        raise NotImplementedError(METHOD_NOT_IMPLEMENTED)
