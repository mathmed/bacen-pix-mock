from http import HTTPStatus
from traceback import format_exc
from typing import Tuple
from uuid import uuid4

from app.core.collections import Auth, Institution
from app.core.constants import ERROR_TO_SAVE
from app.core.helpers.http import HttpError, HttpResponse, HttpStatus
from app.ports.external import DatabasePort, EncryptPort
from app.ports.usecases import (CreateInstitutionParams, CreateInstitutionPort,
                                CreateInstitutionResponse)


class CreateInstitution(CreateInstitutionPort):

    def __init__(self, params: CreateInstitutionParams, database: DatabasePort, encrypt: EncryptPort) -> None:
        self.params = params
        self.database = database
        self.encrypt = encrypt

    def execute(self) -> HttpResponse:

        institution, auth = self._validate_params()
        self._verify_if_ispb_exists()
        self._verify_if_user_exists()
        self._save(institution, auth)

        return HttpStatus.created_201(
            CreateInstitutionResponse(id=self.params.basic_user)
        )

    def _verify_if_user_exists(self):
        user = self.database.get_by_filters(
            'Auth', [{'user': self.params.basic_user}])
        if len(user) > 0:
            raise HttpError(HTTPStatus.BAD_REQUEST,
                            f'User {self.params.basic_user} already exists')

    def _save(self, institution: Institution, auth: Auth):
        try:
            self.database.save(institution)
            self.database.save(auth)
        except Exception:
            print(format_exc())
            raise HttpError(HTTPStatus.BAD_REQUEST,
                            ERROR_TO_SAVE)

    def _verify_if_ispb_exists(self):
        institutions = self.database.get_by_filters(
            'Institution', [{'ispb': self.params.ispb}])
        if len(institutions) > 0:
            raise HttpError(HTTPStatus.BAD_REQUEST,
                            f'Ispb {self.params.ispb} already exists')

    def _validate_params(self) -> Tuple[Institution, Auth]:
        try:
            id = str(uuid4())
            institution = Institution(
                callback_url=self.params.callback_url,
                document=self.params.document,
                ispb=self.params.ispb,
                name=self.params.name,
                id=id
            )
            auth = Auth(
                user=self.params.basic_user,
                password=self.encrypt.encrypt(self.params.basic_password),
                id=id
            )
            return institution, auth
        except AssertionError as e:
            print(format_exc())
            raise HttpError(HTTPStatus.UNPROCESSABLE_ENTITY, str(e))
