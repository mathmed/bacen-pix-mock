from app.core.helpers.http import HttpResponse, HttpStatus
from app.ports.usecases import SendPixParams, SendPixPort


class SendPix(SendPixPort):

    def __init__(self, params: SendPixParams) -> None:
        self.params = params

    def execute(self) -> HttpResponse:
        print('SendPix')
        return HttpStatus.no_content_204()
