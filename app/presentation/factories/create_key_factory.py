from app.core.usecases.create_key import CreateKey, CreateKeyParams
from app.ports.usecases import Usecase


def create_key_factory(params: CreateKeyParams) -> Usecase:
    return CreateKey(params)
