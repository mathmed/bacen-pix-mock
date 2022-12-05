from http import HTTPStatus
from traceback import format_exc

from app.core.collections import Institution
from app.core.helpers.http import HttpError, HttpResponse, HttpStatus
from app.ports.external import DatabasePort
from app.ports.usecases import (CreateInstitutionParams, CreateInstitutionPort,
                                CreateInstitutionResponse)


class CreateInstitution(CreateInstitutionPort):

    def __init__(self, params: CreateInstitutionParams, database: DatabasePort) -> None:
        self.params = params
        self.database = database

    def execute(self) -> HttpResponse:

        dto = self._validate_params()
        self._verify_if_ispb_exists()
        id = self._save_institution(dto)

        return HttpStatus.created_201(
            CreateInstitutionResponse(id=id)
        )

    def _save_institution(self, dto: Institution) -> str:
        try:
            return self.database.save(dto)
        except Exception:
            print(format_exc())
            raise HttpError(HTTPStatus.BAD_REQUEST,
                            'Error to save institution.')

    def _verify_if_ispb_exists(self):
        institutions = self.database.get_by_filters(
            'Institution', [{'ispb': self.params.ispb}])
        if len(institutions) > 0:
            raise HttpError(HTTPStatus.BAD_REQUEST,
                            f'Ispb {self.params.ispb} already exists')

    def _validate_params(self) -> Institution:
        try:
            return Institution(
                callback_url=self.params.callback_url,
                document=self.params.document,
                ispb=self.params.ispb,
                name=self.params.name
            )
        except AssertionError as e:
            print(format_exc())
            raise HttpError(HTTPStatus.UNPROCESSABLE_ENTITY, str(e))
