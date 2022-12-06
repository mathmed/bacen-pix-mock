
from dataclasses import dataclass

from app.core.validators import *

from .account import Account
from .base_collection import BaseCollection


@dataclass
class Pix(BaseCollection):
    from_account: Account
    to_account: Account
    amount: int
    description: str
