from http import HTTPStatus

import pytest
from faker import Faker

from .http import HttpError, HttpRequest, HttpResponse, HttpStatus

sut = HttpStatus()
faker = Faker()


def test_should_return_correct_ok_200():
    body = faker.name()
    result = sut.ok_200(body)
    assert result.status_code == HTTPStatus.OK
    assert result.body == body


def test_should_return_correct_created_201():
    body = faker.name()
    result = sut.created_201(body)
    assert result.status_code == HTTPStatus.CREATED
    assert result.body == body


def test_should_return_correct_accepted_202():
    body = faker.name()
    result = sut.accepted_202(body)
    assert result.status_code == HTTPStatus.ACCEPTED
    assert result.body == body


def test_should_return_correct_no_content_204():
    result = sut.no_content_204()
    assert result.status_code == HTTPStatus.NO_CONTENT


def test_should_return_correct_error_400():
    error = faker.sentence()
    result = sut.bad_request_400(error)
    assert result.status_code == HTTPStatus.BAD_REQUEST
    assert result.body["error"] == error
    result = sut.bad_request_400()
    assert result.status_code == HTTPStatus.BAD_REQUEST
    assert result.body["error"] == "Bad Request"
    body = {'msg': faker.word()}
    result = sut.bad_request_400(body=body)
    assert result.status_code == HTTPStatus.BAD_REQUEST
    assert result.body["msg"] == body['msg']


def test_should_return_correct_unauthorized_401():
    error = faker.sentence()
    result = sut.unauthorized_401(error)
    assert result.status_code == HTTPStatus.UNAUTHORIZED
    assert result.body["error"] == error
    result = sut.unauthorized_401()
    assert result.status_code == HTTPStatus.UNAUTHORIZED
    assert result.body["error"] == "Unauthorized"


def test_should_return_correct_forbidden_403():
    error = faker.sentence()
    result = sut.forbidden_403(error)
    assert result.status_code == HTTPStatus.FORBIDDEN
    assert result.body["error"] == error
    result = sut.forbidden_403()
    assert result.status_code == HTTPStatus.FORBIDDEN
    assert result.body["error"] == "Forbidden"


def test_should_return_correct_not_found_404():
    error = faker.sentence()
    result = sut.not_found_404(error)
    assert result.status_code == HTTPStatus.NOT_FOUND
    assert result.body["error"] == error
    result = sut.not_found_404()
    assert result.status_code == HTTPStatus.NOT_FOUND
    assert result.body["error"] == "Not Found"


def test_should_return_correct_not_allowed_405():
    error = faker.sentence()
    result = sut.not_allowed_405(error)
    assert result.status_code == HTTPStatus.METHOD_NOT_ALLOWED
    assert result.body["error"] == error
    result = sut.not_allowed_405()
    assert result.status_code == HTTPStatus.METHOD_NOT_ALLOWED
    assert result.body["error"] == "Method Not Allowed"


def test_should_return_correct_conflict_409():
    error = faker.sentence()
    result = sut.conflict_409(error)
    assert result.status_code == HTTPStatus.CONFLICT
    assert result.body["error"] == error
    result = sut.conflict_409()
    assert result.status_code == HTTPStatus.CONFLICT
    assert result.body["error"] == "Conflict"


def test_should_return_correct_expection_failed_417():
    error = faker.sentence()
    result = sut.expection_failed_417(error)
    assert result.status_code == HTTPStatus.EXPECTATION_FAILED
    assert result.body["error"] == error
    result = sut.expection_failed_417()
    assert result.status_code == HTTPStatus.EXPECTATION_FAILED
    assert result.body["error"] == "Expectation Failed"


def test_should_return_correct_locked_423():
    error = faker.sentence()
    result = sut.locked_423(error)
    assert result.status_code == HTTPStatus.LOCKED
    assert result.body["error"] == error


def test_should_return_correct_unprocessable_entity_422():
    error = faker.sentence()
    result = sut.unprocessable_entity_422(error)
    assert result.status_code == HTTPStatus.UNPROCESSABLE_ENTITY
    assert result.body["error"] == error
    result = sut.unprocessable_entity_422()
    assert result.status_code == HTTPStatus.UNPROCESSABLE_ENTITY
    assert result.body["error"] == "Unprocessable Entity"


def test_should_return_correct_internal_server_error_500():
    error = faker.sentence()
    result = sut.internal_server_error_500(error)
    assert result.status_code == HTTPStatus.INTERNAL_SERVER_ERROR
    assert result.body["error"] == error
    result = sut.internal_server_error_500()
    assert result.status_code == HTTPStatus.INTERNAL_SERVER_ERROR
    assert result.body["error"] == "Internal Server Error"


def test_should_return_correct_not_implemented_error_501():
    error = faker.sentence()
    result = sut.not_implemented_error_501(error)
    assert result.status_code == HTTPStatus.NOT_IMPLEMENTED
    assert result.body["error"] == error
    result = sut.not_implemented_error_501()
    assert result.status_code == HTTPStatus.NOT_IMPLEMENTED
    assert result.body["error"] == "Not implemented Error"


@pytest.mark.parametrize(
    'error_message, body', [
        (faker.sentence(), None),
        (None, {faker.word: faker.word()})
    ]
)
def test_should_return_correct_bad_gateway_502(
    error_message, body
):
    result = sut.bad_gateway_502(error_message, body)
    assert result.status_code == HTTPStatus.BAD_GATEWAY
    if body:
        assert result.body == body
    else:
        assert result.body["error"] == error_message or HTTPStatus.BAD_GATEWAY.phrase


@pytest.mark.parametrize(
    'error_message, body', [
        (faker.sentence(), None),
        (None, {faker.word: faker.word()})
    ]
)
def test_should_return_correct_service_unavailable_503(
    error_message, body
):
    result = sut.service_unavailable_503(error_message, body)
    assert result.status_code == HTTPStatus.SERVICE_UNAVAILABLE
    if body:
        assert result.body == body
    else:
        assert result.body["error"] == error_message or HTTPStatus.SERVICE_UNAVAILABLE.phrase


def test_should_return_correct_error_406():
    faker_message = faker.sentence()
    result = sut.not_acceptable_406(faker_message)
    assert result.status_code == HTTPStatus.NOT_ACCEPTABLE
    assert result.body["error"] == faker_message

    result = sut.not_acceptable_406()
    assert result.status_code == HTTPStatus.NOT_ACCEPTABLE
    assert result.body["error"] == HTTPStatus.NOT_ACCEPTABLE.phrase

    result = sut.not_acceptable_406(faker_message)
    assert result.status_code == HTTPStatus.NOT_ACCEPTABLE
    assert result.body["error"] == faker_message


def test_should_make_http_error_instance():
    status_code = faker.random_int()
    message = faker.sentence()
    http_error = HttpError(
        status_code=status_code,
        message=message
    )

    assert http_error.status_code == status_code
    assert http_error.message == message
    assert repr(
        http_error) == f'HttpError (status_code={status_code}, message={message})'


def test_should_make_http_response_instance():
    status_code = faker.random_int()
    body = faker.sentence()
    http_response = HttpResponse(
        status_code=status_code,
        body=body
    )

    assert http_response.status_code == status_code
    assert http_response.body == body
    assert repr(
        http_response) == f'HttpResponse (status_code={status_code}, body={body})'


def test_should_make_http_request_instance():
    header = {
        faker.word(): faker.word()
    }
    body = {
        faker.word(): faker.word()
    }
    query = {
        faker.word(): faker.word()
    }
    http_request = HttpRequest(
        header=header,
        body=body,
        query=query
    )

    assert http_request.header == header
    assert http_request.body == body
    assert http_request.query == query
    assert repr(
        http_request) == f'HttpRequest (header={header}, body={body}, query={query})'
