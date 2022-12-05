from typing import Dict, List

from faker import Faker

from app.core.collections import BaseCollection
from app.ports.external import DatabasePort

faker = Faker()


class DatabaseMock(DatabasePort):
    def get_by_filters(
        self,
        collection_name: str,
        filters: List[Dict],
    ) -> List[BaseCollection]:
        return []

    def save(
        self,
        collection: BaseCollection,
    ) -> str:
        return faker.word()

    def delete(self, id: str, collection: str):
        pass
