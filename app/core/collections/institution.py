
from dataclasses import dataclass
from typing import Any

from app.core.helpers.strings import contains_number, validate_cnpj

from .base_collection import BaseCollection


@dataclass
class Institution(BaseCollection):
    name: str
    callback_url: str
    document: str
    ispb: str

    def __setattr__(self, attribute: str, value: Any):

        if attribute == 'name':
            assert 0 < len(
                value) < 50, f'Value of {attribute} must contain between 1 - 50 characters.'
            assert not contains_number(
                value), f'Value of {attribute} must not contain digits.'

        if attribute == 'ispb':
            value: str = str(value)
            assert value.isdigit(), f'Value of {attribute} must be a digit.'
            assert len(
                value) == 8, f'Value of {attribute} must contain 8 characters.'

        if attribute == 'document':
            value: str = str(value)
            assert validate_cnpj(
                value) is True, f'Value of {attribute} must be a valid CNPJ.'

        self.__dict__[attribute] = value
