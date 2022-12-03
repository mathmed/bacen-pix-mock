from app.core.helpers.http import HttpResponse, HttpStatus
from app.ports.usecases import CreateISPBParams, CreateISPBPort


class CreateISPB(CreateISPBPort):

    def __init__(self, params: CreateISPBParams) -> None:
        self.params = params

    def execute(self) -> HttpResponse:
        print('CreateISPB')
        return HttpStatus.no_content_204()
