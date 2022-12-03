from app.core.helpers.http import HttpResponse, HttpStatus
from app.ports.usecases import GetKeyParams, GetKeyPort


class GetKey(GetKeyPort):

    def __init__(self, params: GetKeyParams) -> None:
        self.params = params

    def execute(self) -> HttpResponse:
        print('GetKey')
        return HttpStatus.no_content_204()
