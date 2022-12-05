from app.core.collections import Institution

from .values import *


def make_institution_object() -> Institution:
    return Institution(
        name=person(),
        callback_url=url(),
        ispb=str(integer(10000000, 99999999)),
        document=cnpj()
    )
