from app.core.usecases.get_key import GetKey, GetKeyParams
from app.ports.usecases import Usecase


def get_key_factory(params: GetKeyParams) -> Usecase:
    return GetKey(params)
