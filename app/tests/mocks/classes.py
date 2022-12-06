from typing import Dict, List

from faker import Faker

from app.core.collections import BaseCollection
from app.ports.external import DatabasePort, EncryptPort

faker = Faker()


class EncryptMock(EncryptPort):
    def encrypt(self, password: str) -> str:
        return ''

    def verify(self, encrypted: str, password: str) -> bool:
        return True


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
