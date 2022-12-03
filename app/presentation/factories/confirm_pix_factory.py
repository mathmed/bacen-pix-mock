from app.core.usecases.confirm_pix import ConfirmPix, ConfirmPixParams
from app.ports.usecases import Usecase


def confirm_pix_factory(params: ConfirmPixParams) -> Usecase:
    return ConfirmPix(params)
