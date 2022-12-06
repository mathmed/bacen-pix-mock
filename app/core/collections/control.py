
from dataclasses import dataclass

from .base_collection import BaseCollection


@dataclass
class Control(BaseCollection):
    key: str
    value: str
    created_at: int = None
    updated_at: int = None
    id: str = None
