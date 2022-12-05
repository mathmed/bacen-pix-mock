
from dataclasses import dataclass
from typing import Any

from app.core.enums.enums import AccountTypes, KeyTypes
from app.core.validators import *

from .base_collection import BaseCollection


@dataclass
class Key(BaseCollection):
    key_type: KeyTypes
    key_value: str
    owner_document: str
    owner_name: str
    ispb: str
    branch: str
    account_number: str
    account_type: AccountTypes

    def __setattr__(self, attribute: str, value: Any):

        if attribute == 'owner_name':
            validate_name(value)

        if attribute == 'ispb':
            value = str(value)
            validate_ispb(value)

        if attribute == 'owner_document':
            value = str(value)
            validate_document(value, 'any')

        if attribute == 'key_value':
            if self.key_type == KeyTypes.CPF:
                validate_document(value, 'cpf')
            elif self.key_type == KeyTypes.PHONE:
                validate_phone(value)
            elif self.key_type == KeyTypes.EVP:
                validate_uuid(value)
            elif self.key_type == KeyTypes.EMAIL:
                validate_email(value)

        if attribute == 'branch':
            validate_branch(value)

        if attribute == 'account_number':
            validate_account_number(value)

        self.__dict__[attribute] = value
