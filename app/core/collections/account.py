from dataclasses import dataclass

from app.core.enums.enums import AccountTypes
from app.core.validators import (validate_account_number, validate_branch,
                                 validate_document, validate_ispb,
                                 validate_name)

from .base_collection import BaseCollection


@dataclass
class Account(BaseCollection):
    ispb: str
    branch: str
    account_number: str
    account_type: AccountTypes
    person_name: str
    person_document: str

    def __post_init__(self):
        validate_name(self.person_name)
        validate_ispb(self.ispb)
        validate_document(self.person_document, 'any')
        validate_branch(self.branch)
        validate_account_number(self.account_number)
