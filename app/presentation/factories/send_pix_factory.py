from app.adapters.database import MongoDBAdapter
from app.core.usecases.send_pix import SendPix, SendPixParams
from app.ports.usecases import Usecase


def send_pix_factory(params: SendPixParams) -> Usecase:
    return SendPix(
        params=params,
        database=MongoDBAdapter()
    )
