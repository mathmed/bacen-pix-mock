
from dataclasses import dataclass

from app.core.helpers.validators import (validate_document, validate_ispb,
                                         validate_name)

from .base_collection import BaseCollection


@dataclass
class Institution(BaseCollection):
    name: str
    callback_url: str
    document: str
    ispb: str
    created_at: int = None
    updated_at: int = None
    id: str = None

    def __post_init__(self):
        validate_name(self.name)
        validate_document(self.document, 'cnpj')
        validate_ispb(self.ispb)
