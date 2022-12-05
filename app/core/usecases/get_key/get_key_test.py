from http import HTTPStatus
from unittest.mock import MagicMock

from app.tests.helpers import assert_http_error
from app.tests.helpers.asserts import assert_dict_and_objects
from app.tests.mocks import DatabaseMock, make_key_object, uuid

from .get_key import GetKey, GetKeyParams


def _make_params() -> GetKeyParams:
    return GetKeyParams(
        key=uuid()
    )


def _make_sut() -> GetKey:
    return GetKey(
        database=DatabaseMock(),
        params=_make_params()
    )


def test_get_key_should_raise_error_if_key_not_exists():
    sut = _make_sut()
    sut.database.get_by_filters = MagicMock(
        return_value=[])
    assert_http_error(sut._get_key, HTTPStatus.NOT_FOUND)


def test_get_key_should_return_key_if_key_exists():
    sut = _make_sut()
    key = make_key_object()
    sut.database.get_by_filters = MagicMock(return_value=[key])
    result = sut._get_key()
    assert_dict_and_objects(result, key)


def test_execute_should_works_correctly():
    sut = _make_sut()
    key = make_key_object()
    sut._get_key = MagicMock(return_value=key)
    result = sut.execute()
    assert result.status_code == HTTPStatus.OK
    assert_dict_and_objects(result.body, key)
