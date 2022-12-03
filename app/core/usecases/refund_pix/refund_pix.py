from app.core.helpers.http import HttpResponse, HttpStatus
from app.ports.usecases import RefundPixParams, RefundPixPort


class RefundPix(RefundPixPort):

    def __init__(self, params: RefundPixParams) -> None:
        self.params = params

    def execute(self) -> HttpResponse:
        print('RefundPix')
        return HttpStatus.no_content_204()
