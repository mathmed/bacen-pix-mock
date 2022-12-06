from app.adapters.database import MongoDBAdapter
from app.adapters.encrypt import PasslibAdapter
from app.adapters.jwt import JwtAdapter
from app.core.usecases.auth import Auth, AuthParams
from app.ports.usecases import Usecase


def auth_factory(params: AuthParams) -> Usecase:
    return Auth(
        params=params,
        database=MongoDBAdapter(),
        encrypt=PasslibAdapter(),
        jwt=JwtAdapter()
    )
