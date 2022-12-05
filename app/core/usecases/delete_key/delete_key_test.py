from http import HTTPStatus
from unittest.mock import MagicMock

from app.tests.helpers import assert_http_error
from app.tests.helpers.asserts import assert_dict_and_objects
from app.tests.mocks import DatabaseMock, make_key_object, uuid

from .delete_key import DeleteKey, DeletetKeyParams


def _make_params() -> DeletetKeyParams:
    return DeletetKeyParams(
        key=uuid()
    )


def _make_sut() -> DeleteKey:
    return DeleteKey(
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


def test_delete_key_should_raise_error_on_error_to_delete():
    sut = _make_sut()
    sut.database.delete = MagicMock(
        side_effect=Exception)
    assert_http_error(sut._delete_key, HTTPStatus.BAD_REQUEST, uuid())


def test_delete_key_should_pass_on_success():
    sut = _make_sut()
    sut.database.delete = MagicMock()
    assert sut._delete_key(uuid()) is None


def test_execute_should_works_correctly():
    sut = _make_sut()
    key = make_key_object()
    sut._get_key = MagicMock(return_value=key)
    sut._delete_key = MagicMock(return_value=True)
    result = sut.execute()
    assert result.status_code == HTTPStatus.NO_CONTENT
