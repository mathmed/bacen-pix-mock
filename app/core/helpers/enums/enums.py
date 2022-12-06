from enum import Enum


class KeyTypes(str, Enum):
    CPF = 'CPF'
    PHONE = 'PHONE'
    EMAIL = 'EMAIL'
    EVP = 'EVP'


class AccountTypes(str, Enum):
    CHECKING_ACCOUNT = 'CACC'
    SAVINGS_ACCOUNT = 'SVGS'
    PAYMENT_ACCOUNT = 'TRAN'
    SALARY_ACCOUNT = 'SLRY'


class PixTypes(str, Enum):
    MANUAL = 'MANUAL'
    DICT = 'DICT'


class PixStatus(str, Enum):
    PENDING = 'PENDING'
    CONFIRMED = 'CONFIRMED'
    APPROVED = 'CONFIRMED'
    REJECTED = 'REJECTED'
