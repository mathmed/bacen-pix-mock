from http import HTTPStatus
from traceback import format_exc

from app.core.collections import Account, Pix
from app.core.helpers.enums import PixStatus, PixTypes
from app.core.helpers.http import HttpError, HttpResponse, HttpStatus
from app.core.helpers.strings import generate_end_to_end_id
from app.core.helpers.token import get_token
from app.ports.external import DatabasePort
from app.ports.usecases import SendPixParams, SendPixPort


class SendPix(SendPixPort):

    def __init__(self, params: SendPixParams, database: DatabasePort) -> None:
        self.params = params
        self.database = database

    def execute(self) -> HttpResponse:

        pix = self._validate_params()
        self._verify_ispb()
        print(pix)

        self._save_pix(pix)
        return HttpStatus.no_content_204()

    def _save_pix(self, dto: Pix) -> str:
        try:
            return self.database.save(dto)
        except Exception:
            print(format_exc())
            raise HttpError(HTTPStatus.BAD_REQUEST,
                            'Error to save Pix.')

    def _verify_ispb(self):
        if self.params.to_ispb == get_token().ispb:
            raise HttpError(HTTPStatus.NOT_ACCEPTABLE,
                            f'Cannot send Pix to same ISPB')

    def _validate_params(self) -> Pix:
        try:

            from_ispb = get_token().ispb

            from_account = Account(
                **self.params.from_account.__dict__, ispb=from_ispb)
            to_account = Account(
                **self.params.to_account.__dict__, ispb=self.params.to_ispb)

            if self.params.pix_type == PixTypes.DICT and (not self.params.to_key or not self.params.to_key_type):
                raise HttpError(HTTPStatus.UNPROCESSABLE_ENTITY,
                                f'toKey and toKeyType are required on DICT type PIX')

            return Pix(
                amount=self.params.amount,
                description=self.params.description,
                from_account=from_account,
                to_account=to_account,
                to_key_type=self.params.to_key_type,
                to_key=self.params.to_key,
                status=PixStatus.PENDING,
                pix_type=self.params.pix_type,
                end2end_id=generate_end_to_end_id(from_ispb)
            )
        except AssertionError as e:
            print(format_exc())
            raise HttpError(HTTPStatus.UNPROCESSABLE_ENTITY, str(e))
