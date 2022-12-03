from app.core.usecases.create_ispb import CreateISPB, CreateISPBParams
from app.ports.usecases import Usecase


def create_ispb_factory(params: CreateISPBParams) -> Usecase:
    return CreateISPB(params)
