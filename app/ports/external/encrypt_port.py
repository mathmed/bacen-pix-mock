from abc import ABC, abstractmethod

from app.core.constants import NOT_IMPLEMENTED_ERROR


class EncryptPort(ABC):

    @abstractmethod
    def encrypt(self, password: str) -> str:
        raise NotImplementedError(NOT_IMPLEMENTED_ERROR)

    @abstractmethod
    def verify(self, encrypted: str, password: str) -> bool:
        raise NotImplementedError(NOT_IMPLEMENTED_ERROR)
