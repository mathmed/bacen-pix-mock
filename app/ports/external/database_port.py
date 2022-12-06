from abc import ABC, abstractmethod
from typing import Any, Dict, List

from app.core.collections import BaseCollection
from app.core.constants import NOT_IMPLEMENTED_ERROR


class DatabasePort(ABC):

    @abstractmethod
    def get_by_filters(
        self,
        collection_name: str,
        filters: List[Dict],
    ) -> List[Any]:
        raise NotImplementedError(NOT_IMPLEMENTED_ERROR)

    @abstractmethod
    def save(
        self,
        collection: BaseCollection,
    ) -> str:
        raise NotImplementedError(NOT_IMPLEMENTED_ERROR)

    @abstractmethod
    def delete(
        self,
        id: str,
        collection: str,
    ):
        raise NotImplementedError(NOT_IMPLEMENTED_ERROR)
