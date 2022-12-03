
from typing import Any

from fastapi import Response

from app.core.helpers.http import HttpError
from app.ports.usecases import Usecase


def fastapi_adapter(response: Response, usecase: Usecase) -> Any:
    try:
        usecase_response = usecase.execute()
        response.status_code = usecase_response.status_code
        return usecase_response.body if usecase_response.body else response
    except HttpError as error:
        response.status_code = error.status_code
        return {'message': error.message} if error.message else response

    except Exception:
        return {'message': 'Internal server error'}
