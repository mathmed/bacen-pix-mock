
from dataclasses import dataclass

from app.core.validators.validators import validate_uuid

from .base_collection import BaseCollection


@dataclass
class Token(BaseCollection):
    ispb: str
    exp: int
    iat: int
    iss: str


@dataclass
class Auth(BaseCollection):
    user: str
    password: str
    created_at: int = None
    updated_at: int = None
    id: str = None

    def __post_init__(self):
        validate_uuid(self.user)
