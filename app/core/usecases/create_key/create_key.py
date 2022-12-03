from app.core.helpers.http import HttpResponse, HttpStatus
from app.ports.usecases import CreateKeyParams, CreateKeyPort


class CreateKey(CreateKeyPort):

    def __init__(self, params: CreateKeyParams) -> None:
        self.params = params

    def execute(self) -> HttpResponse:
        print('CreateKey')
        return HttpStatus.no_content_204()
