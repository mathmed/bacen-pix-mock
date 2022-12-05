
from http import HTTPStatus
from traceback import format_exc
from typing import Any

from fastapi import Response

from app.core.helpers.http import HandledError, HttpError
from app.ports.usecases import Usecase


def fastapi_adapter(response: Response, usecase: Usecase) -> Any:
    try:
        usecase_response = usecase.execute()
        response.status_code = usecase_response.status_code
        return usecase_response.body if usecase_response.body else response
    except HttpError as error:
        response.status_code = error.status_code
        return HandledError(message=error.message) if error.message else response

    except Exception:
        print(format_exc())
        response.status_code = HTTPStatus.INTERNAL_SERVER_ERROR
        return HandledError(message='Internal server error')
