from app.core.usecases.refund_pix import RefundPix, RefundPixParams
from app.ports.usecases import Usecase


def refund_pix_factory(params: RefundPixParams) -> Usecase:
    return RefundPix(params)
