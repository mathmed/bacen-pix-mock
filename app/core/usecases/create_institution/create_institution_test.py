from http import HTTPStatus
from unittest.mock import MagicMock

from app.tests.helpers import assert_http_error
from app.tests.mocks import (DatabaseMock, EncryptMock, cnpj, integer,
                             make_auth_object, make_institution_object, person,
                             url, uuid, word)

from .create_institution import CreateInstitution, CreateInstitutionParams


def _make_params() -> CreateInstitutionParams:
    return CreateInstitutionParams(
        name=person(),
        callback_url=url(),
        ispb=str(integer(10000000, 99999999)),
        document=cnpj(),
        basic_user=uuid(),
        basic_password=word(),
    )


def _make_sut() -> CreateInstitution:
    return CreateInstitution(
        database=DatabaseMock(),
        params=_make_params(),
        encrypt=EncryptMock()
    )


def test_save_institution_should_raise_exception_on_error_to_save():
    sut = _make_sut()
    sut.database.save = MagicMock(side_effect=Exception)
    assert_http_error(sut._save,
                      HTTPStatus.BAD_REQUEST, make_institution_object(), make_auth_object())


def test_save_institution_should_return_id_on_success():
    sut = _make_sut()
    sut.database.save = MagicMock(return_value=uuid())
    assert sut._save(make_institution_object(), make_auth_object()) is None


def test_verify_if_ispb_exists_should_raise_error_if_ispb_exists():
    sut = _make_sut()
    sut.database.get_by_filters = MagicMock(
        return_value=[make_institution_object()])
    assert_http_error(sut._verify_if_ispb_exists, HTTPStatus.BAD_REQUEST)


def test_verify_if_ispb_exists_should_pass_if_ispb_not_exists():
    sut = _make_sut()
    sut.database.get_by_filters = MagicMock(return_value=[])
    assert sut._verify_if_ispb_exists() is None


def test_verify_if_user_exists_should_raise_error_if_user_exists():
    sut = _make_sut()
    sut.database.get_by_filters = MagicMock(
        return_value=[make_auth_object()])
    assert_http_error(sut._verify_if_user_exists, HTTPStatus.BAD_REQUEST)


def test_verify_if_user_exists_should_pass_if_user_not_exists():
    sut = _make_sut()
    sut.database.get_by_filters = MagicMock(return_value=[])
    assert sut._verify_if_user_exists() is None


def test_validate_params_should_raise_error_on_invalid_dto_params():
    sut = _make_sut()
    sut.params.document = word()
    assert_http_error(sut._validate_params, HTTPStatus.UNPROCESSABLE_ENTITY)


def test_validate_params_should_return_correct_dto_on_valid_params():
    sut = _make_sut()
    sut._validate_params()
    institution, auth = sut._validate_params()
    assert institution.name == sut.params.name
    assert institution.document == sut.params.document
    assert institution.ispb == sut.params.ispb
    assert institution.callback_url == sut.params.callback_url
    assert auth.user == sut.params.basic_user


def test_execute_should_works_correctly():
    sut = _make_sut()
    sut._save = MagicMock(return_value=uuid())
    sut._verify_if_ispb_exists = MagicMock(return_value=None)
    sut._validate_params = MagicMock(return_value=(
        make_institution_object(), make_auth_object()))
    assert sut.execute().status_code == HTTPStatus.CREATED
