from app.adapters.database import MongoDBAdapter
from app.core.usecases.create_institution import (CreateInstitution,
                                                  CreateInstitutionParams)
from app.ports.usecases import Usecase


def create_institution_factory(params: CreateInstitutionParams) -> Usecase:
    return CreateInstitution(
        params=params,
        database=MongoDBAdapter()
    )
