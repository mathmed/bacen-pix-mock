
from dataclasses import dataclass
from typing import Optional

from app.core.helpers.enums import KeyTypes, PixStatus, PixTypes
from app.core.helpers.validators import *

from .account import Account
from .base_collection import BaseCollection


@dataclass
class Pix(BaseCollection):
    end2end_id: str
    from_account: Account
    to_account: Account
    amount: int
    description: str
    status: PixStatus
    pix_type: PixTypes
    to_key: Optional[str] = None
    to_key_type: Optional[KeyTypes] = None
    created_at: int = None
    updated_at: int = None
    id: str = None

    def __post_init__(self):
        validate_amount(self.amount)
        if self.to_key_type == KeyTypes.CPF:
            return validate_document(self.to_key or '', 'cpf')
        elif self.to_key_type == KeyTypes.PHONE:
            return validate_phone(self.to_key or '')
        elif self.to_key_type == KeyTypes.EVP:
            return validate_uuid(self.to_key or '')
        elif self.to_key_type == KeyTypes.EMAIL:
            return validate_email(self.to_key or '')
