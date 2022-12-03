from app.core.usecases.get_pix import GetPix, GetPixParams
from app.ports.usecases import Usecase


def get_pix_factory(params: GetPixParams) -> Usecase:
    return GetPix(params)
