from abc import ABC, abstractmethod
from typing import Any, Dict, List

from app.core.collections import BaseCollection

METHOD_NOT_IMPLEMENTED = 'Method not implemented'


class DatabasePort(ABC):

    @abstractmethod
    def get_by_filters(
        self,
        collection_name: str,
        filters: List[Dict],
    ) -> List[Any]:
        raise NotImplementedError(METHOD_NOT_IMPLEMENTED)

    @abstractmethod
    def save(
        self,
        collection: BaseCollection,
    ) -> str:
        raise NotImplementedError(METHOD_NOT_IMPLEMENTED)

    @abstractmethod
    def delete(
        self,
        id: str,
        collection: str,
    ):
        raise NotImplementedError(METHOD_NOT_IMPLEMENTED)
