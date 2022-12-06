
from dataclasses import dataclass

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
    created_at: int = None
    updated_at: int = None
    id: str = None

    def __post_init__(self):
        validate_name(self.owner_name)
        validate_document(self.owner_document, 'any')
        validate_ispb(self.ispb)
        validate_branch(self.branch)
        validate_account_number(self.account_number)
        if self.key_type == KeyTypes.CPF:
            return validate_document(self.key_value, 'cpf')
        elif self.key_type == KeyTypes.PHONE:
            return validate_phone(self.key_value)
        elif self.key_type == KeyTypes.EVP:
            return validate_uuid(self.key_value)
        elif self.key_type == KeyTypes.EMAIL:
            return validate_email(self.key_value)
