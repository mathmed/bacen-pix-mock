from abc import ABC, abstractmethod

METHOD_NOT_IMPLEMENTED = 'Method not implemented'


class EncryptPort(ABC):

    @abstractmethod
    def encrypt(self, password: str) -> str:
        raise NotImplementedError(METHOD_NOT_IMPLEMENTED)

    @abstractmethod
    def verify(self, encrypted: str, password: str) -> bool:
        raise NotImplementedError(METHOD_NOT_IMPLEMENTED)
