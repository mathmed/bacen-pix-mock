from app.core.helpers.http import HttpResponse, HttpStatus
from app.ports.usecases import GetPixParams, GetPixPort


class GetPix(GetPixPort):

    def __init__(self, params: GetPixParams) -> None:
        self.params = params

    def execute(self) -> HttpResponse:
        print('GetPix')
        return HttpStatus.no_content_204()
