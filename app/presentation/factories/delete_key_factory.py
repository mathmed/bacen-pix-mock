from app.adapters.database import MongoDBAdapter
from app.core.usecases.delete_key import DeleteKey, DeletetKeyParams
from app.ports.usecases import Usecase


def delete_key_factory(params: DeletetKeyParams) -> Usecase:
    return DeleteKey(
        params=params,
        database=MongoDBAdapter()
    )
