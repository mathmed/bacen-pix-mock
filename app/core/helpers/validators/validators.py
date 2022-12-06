from re import match

from app.core.helpers.strings import (contains_number, validate_cnpj,
                                      validate_cpf)


def validate_amount(amount: int):
    assert isinstance(amount, int), f'Value of `amount` must be a integer.'
    assert amount > 0, f'Value of `amount` must be > 0.'


def validate_name(name: str):
    assert 0 < len(
        name) < 50, f'Value of `name` must contain between 1 - 50 characters.'
    assert not contains_number(
        name), f'Value of `name` must not contain digits.'


def validate_ispb(ispb: str):
    ispb: str = str(ispb)
    assert ispb.isdigit(), f'Value of `ispb` must be a digit.'
    assert len(ispb) == 8, f'Value of `ispb` must contain 8 characters.'


def validate_document(document: str, document_type: str):

    if document_type == 'any':
        valid = validate_cnpj(document) or validate_cpf(document)
        assert valid is True, f'Value of `document` must be a valid CNPJ/CNPJ.'

    elif document_type == 'cnpj':
        document: str = str(document)
        assert validate_cnpj(
            document) is True, f'Value of `document` must be a valid CNPJ.'

    elif document_type == 'cpf':
        document: str = str(document)
        assert validate_cpf(
            document) is True, f'Value of `document` must be a valid CPF.'


def validate_phone(phone: str):
    is_valid = match(r'^\+[1-9][0-9]\d{1,14}$', phone)
    assert bool(is_valid) is True, f'Value of `phone` must be a valid Phone.'


def validate_uuid(uuid: str):
    is_valid = match(
        r'[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}', str(uuid))
    assert bool(is_valid) is True, f'Value of `uuid` must be a valid uuid4.'


def validate_email(email: str):
    is_valid = match(
        r"^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$", email)
    assert bool(is_valid) is True, f'Value of `email` must be a valid Email.'


def validate_branch(branch: str):
    branch: str = str(branch)
    assert branch.isdigit(), f'Value of `branch` must be a digit.'
    assert 0 < len(
        branch) <= 4, f'Value of `branch` must contain between 1 and 4 digits'


def validate_account_number(account: str):
    account: str = str(account)
    assert account.isdigit(), f'Value of `account_number` must be a digit.'
    assert 0 < len(
        account) <= 16, f'Value of `branch` must contain between 1 and 16 digits'
