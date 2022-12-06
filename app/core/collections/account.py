from dataclasses import dataclass

from app.core.helpers.enums.enums import AccountTypes
from app.core.helpers.validators import (validate_account_number,
                                         validate_branch, validate_document,
                                         validate_ispb, validate_name)

from .base_collection import BaseCollection


@dataclass
class Account(BaseCollection):
    ispb: str
    branch: str
    number: str
    type: AccountTypes
    owner_name: str
    owner_document: str

    def __post_init__(self):
        validate_name(self.owner_name)
        validate_ispb(self.ispb)
        validate_document(self.owner_document, 'any')
        validate_branch(self.branch)
        validate_account_number(self.number)
