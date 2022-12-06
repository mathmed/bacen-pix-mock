from typing import Dict, List

from faker import Faker

from app.core.collections import Auth, BaseCollection, Token
from app.ports.external import DatabasePort, EncryptPort, JwtPort
from app.tests.mocks.objects import make_token_object
from app.tests.mocks.values import word

faker = Faker()


class JwtMock(JwtPort):
    def encode_bearer(self, auth: Auth, ispb: str, key: str) -> str:
        return word()

    def decode_bearer(self, bearer: str, key: str) -> Token:
        return make_token_object()


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
