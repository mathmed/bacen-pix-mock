from enum import Enum
from http import HTTPStatus
from typing import List

from fastapi import Response

from app.adapters.http import fastapi_adapter
from app.core.helpers.http import HandledError
from app.main import app
from app.ports.usecases.create_institution_port import (
    CreateInstitutionParams, CreateInstitutionResponse)
from app.presentation.factories import create_institution_factory

TAGS: List[str | Enum] = ['Instituição (ISPB)']
PREFIX = '/institution'


@app.post(
    PREFIX,
    status_code=HTTPStatus.CREATED,
    summary='Cadastrar nova Instituição (ISPB)',
    responses={
        HTTPStatus.CREATED.value: {
            'model': CreateInstitutionResponse
        },
        HTTPStatus.BAD_REQUEST.value: {
            'model': HandledError
        }
    },
    tags=TAGS
)
def create_institution(response: Response, body: CreateInstitutionParams):
    return fastapi_adapter(response, create_institution_factory(body))
