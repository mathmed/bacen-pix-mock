from http import HTTPStatus
from unittest.mock import MagicMock

from app.tests.helpers import assert_dict_and_objects, assert_http_error
from app.tests.mocks import (DatabaseMock, EncryptMock, JwtMock, integer,
                             make_auth_object, make_control_object,
                             make_institution_object, make_token_object, word)

from .auth import Auth, AuthParams


def _make_params() -> AuthParams:
    return AuthParams(
        ispb=str(integer(10000000, 99999999)),
        password=word(),
        user=word()
    )


def _make_sut() -> Auth:
    return Auth(
        database=DatabaseMock(),
        params=_make_params(),
        encrypt=EncryptMock(),
        jwt=JwtMock()
    )


def test_make_token_should_raise_error_on_error_to_make_token():
    sut = _make_sut()
    sut.jwt.encode_bearer = MagicMock(side_effect=Exception)
    assert_http_error(sut._make_token,
                      HTTPStatus.UNAUTHORIZED, make_auth_object())


def test_make_token_should_return_encoded_token_on_success():
    sut = _make_sut()
    token = word()
    sut._get_jwt_key = MagicMock(return_value=word())
    sut.jwt.encode_bearer = MagicMock(return_value=token)
    assert sut._make_token(make_auth_object()) == token


def test_verify_user_should_raise_error_if_user_not_exists():
    sut = _make_sut()
    sut.database.get_by_filters = MagicMock(return_value=[])
    assert_http_error(sut._verify_user, HTTPStatus.UNAUTHORIZED)


def test_verify_user_should_raise_error_on_invalid_password_or_ispb():
    sut = _make_sut()
    user = make_auth_object()
    sut.encrypt.verify = MagicMock(return_value=False)
    sut.database.get_by_filters = MagicMock(return_value=[user])
    assert_http_error(sut._verify_user, HTTPStatus.UNAUTHORIZED)


def test_verify_user_should_pass_on_valid_password_and_ispb():
    sut = _make_sut()
    user = make_auth_object()
    sut.encrypt.verify = MagicMock(return_value=True)
    sut._verify_institution = MagicMock(return_value=True)
    sut.database.get_by_filters = MagicMock(return_value=[user])
    assert_dict_and_objects(sut._verify_user(), user)


def test_verify_if_ispb_exists_should_raise_error_if_ispb_not_exists():
    sut = _make_sut()
    sut.database.get_by_filters = MagicMock(
        return_value=[])
    assert sut._verify_institution(make_auth_object()) is False


def test_verify_if_ispb_exists_should_pass_if_ispb_exists():
    sut = _make_sut()
    institution = make_institution_object()
    institution.ispb = sut.params.ispb
    sut.database.get_by_filters = MagicMock(
        return_value=[institution])
    assert sut._verify_institution(make_auth_object()) is True


def test_get_jwt_key_should_throw_error_if_key_not_exists():
    sut = _make_sut()
    sut.database.get_by_filters = MagicMock(return_value=[])
    assert_http_error(sut._get_jwt_key, HTTPStatus.UNAUTHORIZED)


def test_get_jwt_key_should_return_key_on_success():
    sut = _make_sut()
    control_object = make_control_object()
    sut.database.get_by_filters = MagicMock(return_value=[control_object])
    assert sut._get_jwt_key() == control_object.value


def test_execute_should_works_correctly():
    sut = _make_sut()
    sut._verify_user = MagicMock(return_value=make_auth_object())
    sut._make_token = MagicMock(return_value=make_token_object())
    assert sut.execute().status_code == HTTPStatus.OK
