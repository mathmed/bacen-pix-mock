from typing import Optional


class EntityNotFound(Exception):
    """Exception raised for errors on find some Entity on Database"""

    def __init__(self, collection: str, id: Optional[str] = ''):
        self.message = f'Entity {collection} not found on DB. ID: {id}'
        super().__init__(self.message)


class SaveError(Exception):
    """Exception raised for errors on save some Entity on Database"""

    def __init__(self, collection: str, id: Optional[str] = ''):
        self.message = f'Entity {collection} could not be saved on DB. ID: {id}'
        super().__init__(self.message)
