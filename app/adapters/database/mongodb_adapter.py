

from os import getenv
from traceback import format_exc
from typing import Dict, List
from uuid import uuid4

from pymongo import MongoClient
from pymongo.collection import Collection
from pymongo.database import Database

from app.core.collections import BaseCollection
from app.core.errors.database_errors import EntityNotFound, SaveError
from app.ports.external.database_port import DatabasePort


class MongoDBAdapter(DatabasePort):

    _instance: DatabasePort = None
    _client: MongoClient = None
    _database: Database = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = object.__new__(cls)
        return cls._instance

    def __init__(self):
        if not self._client:
            self._client = MongoClient(getenv('MONGO_CONNECTION_URL'))
            self._database = self._client[getenv('MONGO_DATABASE', '')]

    def _get_db(self) -> Database:
        return self._database

    def get_by_filters(
        self,
        collection_name: str,
        filters: List[Dict],
    ) -> List[BaseCollection]:
        try:
            query = {}
            for filter in filters:
                query = query | filter

            collection_instance: Collection = self._get_db()[collection_name]
            items = collection_instance.find(query)

            from app.core import collections
            klass = getattr(collections, collection_name)

            return [BaseCollection.class_from_dict(klass, item) for item in items]
        except Exception:
            print(format_exc())
            raise EntityNotFound(collection_name)

    def save(
        self,
        collection: BaseCollection,
    ) -> str:
        id = str(uuid4())
        collection_name = collection.collection()
        try:
            collection_instance: Collection = self._get_db()[collection_name]
            data = collection.to_dict()
            data['_id'] = id
            return str(collection_instance.insert_one(data).inserted_id)
        except Exception:
            print(format_exc())
            raise SaveError(collection_name, id)
