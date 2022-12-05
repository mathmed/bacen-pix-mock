from http import HTTPStatus
from unittest.mock import MagicMock

from app.core.enums import AccountTypes, KeyTypes
from app.ports.usecases.create_key_port import Account, Owner
from app.tests.helpers import assert_http_error
from app.tests.mocks import (DatabaseMock, cpf, integer, make_key_object,
                             person, uuid, word)
from app.tests.mocks.objects import make_institution_object

from .create_key import CreateKey, CreateKeyParams


def _make_params() -> CreateKeyParams:
    return CreateKeyParams(
        account=Account(
            account_number=str(integer(1, 9999999999999999)),
            account_type=AccountTypes.PAYMENT_ACCOUNT,
            branch=str(integer(1, 9999)),
            ispb=str(integer(10000000, 99999999)),
        ),
        owner=Owner(
            document=cpf(),
            name=person()
        ),
        key=uuid(),
        key_type=KeyTypes.EVP
    )


def _make_sut() -> CreateKey:
    return CreateKey(
        database=DatabaseMock(),
        params=_make_params()
    )


def test_save_key_should_raise_exception_on_error_to_save():
    sut = _make_sut()
    sut.database.save = MagicMock(side_effect=Exception)
    assert_http_error(sut._save_key,
                      HTTPStatus.BAD_REQUEST, make_key_object())


def test_save_key_should_return_id_on_success():
    sut = _make_sut()
    id = uuid()
    sut.database.save = MagicMock(return_value=id)
    assert sut._save_key(make_key_object()) == id


def test_verify_if_ispb_exists_should_raise_error_if_ispb_not_exists():
    sut = _make_sut()
    sut.database.get_by_filters = MagicMock(
        return_value=[])
    assert_http_error(sut._verify_if_ispb_exists, HTTPStatus.NOT_FOUND)


def test_verify_if_ispb_exists_should_pass_if_ispb_exists():
    sut = _make_sut()
    sut.database.get_by_filters = MagicMock(
        return_value=[make_institution_object()])
    assert sut._verify_if_ispb_exists() is None


def test_validate_params_should_return_correct_dto_on_valid_params():
    sut = _make_sut()
    sut._validate_params()
    result = sut._validate_params()
    assert result.account_number == sut.params.account.account_number
    assert result.branch == sut.params.account.branch
    assert result.account_type == sut.params.account.account_type
    assert result.ispb == sut.params.account.ispb
    assert result.owner_document == sut.params.owner.document
    assert result.owner_name == sut.params.owner.name
    assert result.key_value == sut.params.key
    assert result.key_type == sut.params.key_type


def test_validate_params_should_raise_error_on_invalid_dto_params():
    sut = _make_sut()
    sut.params.account.ispb = word()
    assert_http_error(sut._validate_params, HTTPStatus.UNPROCESSABLE_ENTITY)


def test_verify_if_key_exists_should_raise_error_if_key_exists():
    sut = _make_sut()
    sut.database.get_by_filters = MagicMock(
        return_value=[make_key_object()])
    assert_http_error(sut._verify_if_key_exists, HTTPStatus.CONFLICT)


def test_verify_if_key_exists_should_pass_if_key_not_exists():
    sut = _make_sut()
    sut.database.get_by_filters = MagicMock(return_value=[])
    assert sut._verify_if_key_exists() is None


def test_execute_should_works_correctly():
    sut = _make_sut()
    sut._save_key = MagicMock(return_value=uuid())
    sut._verify_if_ispb_exists = MagicMock(return_value=None)
    sut._verify_if_key_exists = MagicMock(return_value=None)
    sut._validate_params = MagicMock(return_value=make_key_object())
    assert sut.execute().status_code == HTTPStatus.CREATED
