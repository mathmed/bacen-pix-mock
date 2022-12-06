from typing import Optional
from uuid import uuid4

from faker import Faker
from faker.providers import internet
from faker.providers import person as faker_person
from faker.providers import ssn

faker = Faker('pt_BR')
faker.add_provider(ssn)
faker.add_provider(faker_person)
faker.add_provider(internet)


def word() -> str:
    return faker.word()


def integer(min: Optional[int] = 0, max: Optional[int] = 9999999999) -> int:
    return faker.random_int(min=min, max=max)


def cnpj() -> str:
    return faker.cnpj().replace('-', '').replace('.', '').replace('/', '')


def cpf() -> str:
    return faker.cpf().replace('-', '').replace('.', '')


def person() -> str:
    return faker.name()


def url() -> str:
    return faker.url()


def uuid() -> str:
    return str(uuid4())
