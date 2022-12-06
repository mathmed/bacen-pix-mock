from app.core.collections import *
from app.core.helpers.enums import AccountTypes, KeyTypes

from .values import *


def make_institution_object() -> Institution:
    return Institution(
        name=person(),
        callback_url=url(),
        ispb=str(integer(10000000, 99999999)),
        document=cnpj()
    )


def make_auth_object() -> Auth:
    return Auth(
        user=uuid(),
        password=word()
    )


def make_token_object() -> Token:
    return Token(
        exp=integer(),
        iat=integer(),
        iss=word(),
        ispb=str(integer(10000000, 99999999)),
        user_id=uuid()
    )


def make_control_object() -> Control:
    return Control(
        key=word(),
        value=word()
    )


def make_key_object() -> Key:
    return Key(
        account_number=str(integer(1, 9999999999999999)),
        account_type=AccountTypes.PAYMENT_ACCOUNT,
        branch=str(integer(1, 9999)),
        ispb=str(integer(10000000, 99999999)),
        key_type=KeyTypes.EVP,
        key_value=uuid(),
        owner_document=cpf(),
        owner_name=person()
    )
