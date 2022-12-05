
from dataclasses import fields
from time import time
from typing import Any, Dict

from app.core.helpers.strings import to_dict_camel_case, to_dict_snake_case


class BaseCollection:
    def to_dict(self) -> Dict:
        self.created_at = int(time())
        self.updated_at = int(time())
        return to_dict_camel_case(self.__dict__)

    def collection(self) -> str:
        return self.__class__.__name__

    @staticmethod
    def class_from_dict(class_name: Any, dict: Dict):
        dict = to_dict_snake_case(dict)
        field_set = {f.name for f in fields(class_name) if f.init}
        filtered_arg_dict = {key: value for key,
                             value in dict.items() if key in field_set}
        return class_name(**filtered_arg_dict)
