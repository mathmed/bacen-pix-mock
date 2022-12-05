from abc import ABC, abstractmethod
from typing import Dict, List

from app.core.collections import BaseCollection

METHOD_NOT_IMPLEMENTED = 'Method not implemented'


class DatabasePort(ABC):

    @abstractmethod
    def get_by_filters(
        self,
        collection_name: str,
        filters: List[Dict],
    ) -> List[BaseCollection]:
        raise NotImplementedError(METHOD_NOT_IMPLEMENTED)

    @abstractmethod
    def save(
        self,
        collection: BaseCollection,
    ) -> str:
        raise NotImplementedError(METHOD_NOT_IMPLEMENTED)
