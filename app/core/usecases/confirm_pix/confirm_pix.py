from app.core.helpers.http import HttpResponse, HttpStatus
from app.ports.usecases import ConfirmPixParams, ConfirmPixPort


class ConfirmPix(ConfirmPixPort):

    def __init__(self, params: ConfirmPixParams) -> None:
        self.params = params

    def execute(self) -> HttpResponse:
        print('ConfirmPix')
        return HttpStatus.no_content_204()
