from abc import ABC, abstractmethod
from typing import Any, Optional

from pydantic import BaseModel

from app.core.constants import NOT_IMPLEMENTED_ERROR
from app.core.helpers.http import HttpResponse
from app.core.helpers.strings import to_camel_case


class BaseClassConfig:
    allow_population_by_field_name = True
    alias_generator = to_camel_case


class InputData(BaseModel):
    class Config(BaseClassConfig):
        pass


class Usecase(ABC):
    @abstractmethod
    def execute(self, *args: Optional[Any]) -> HttpResponse:
        raise NotImplementedError(NOT_IMPLEMENTED_ERROR)
