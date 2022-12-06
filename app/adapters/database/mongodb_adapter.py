

from os import getenv
from time import time
from traceback import format_exc
from typing import Any, Dict, List
from uuid import uuid4

from pymongo import MongoClient
from pymongo.collection import Collection
from pymongo.database import Database

from app.core.collections import BaseCollection
from app.core.errors.database_errors import (DeleteError, EntityNotFound,
                                             SaveError)
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
    ) -> List[Any]:
        try:
            query = {}
            for filter in filters:
                query = query | filter

            collection_instance: Collection = self._get_db()[collection_name]
            items = collection_instance.find(query)

            from app.core import collections
            klass: BaseCollection = getattr(collections, collection_name)

            def mount_collection(item: Dict):
                item['id'] = item['_id']
                return BaseCollection.class_from_dict(klass, item)

            return [mount_collection(item) for item in items]
        except Exception:
            print(format_exc())
            raise EntityNotFound(collection_name)

    def save(
        self,
        collection: BaseCollection,
    ) -> str:
        id = collection.id or str(uuid4())
        collection_name = collection.collection()
        try:
            collection_instance: Collection = self._get_db()[collection_name]
            data = collection.to_dict()
            timestamp = int(time())

            del data['id']

            data['_id'] = id
            data['createdAt'] = timestamp
            data['updatedAt'] = timestamp
            return str(collection_instance.insert_one(data).inserted_id)
        except Exception:
            print(format_exc())
            raise SaveError(collection_name, id)

    def delete(
        self,
        id: str,
        collection: str,
    ):
        try:
            collection_instance: Collection = self._get_db()[collection]
            collection_instance.delete_one({'_id': id})
        except Exception:
            print(format_exc())
            raise DeleteError(collection, id)
