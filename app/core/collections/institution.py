
from dataclasses import dataclass
from typing import Any

from app.core.validators import validate_document, validate_ispb, validate_name

from .base_collection import BaseCollection


@dataclass
class Institution(BaseCollection):
    name: str
    callback_url: str
    document: str
    ispb: str

    def __setattr__(self, attribute: str, value: Any):

        if attribute == 'name':
            validate_name(value)

        if attribute == 'ispb':
            value = str(value)
            validate_ispb(value)

        if attribute == 'document':
            value = str(value)
            validate_document(value, 'any')

        self.__dict__[attribute] = value
