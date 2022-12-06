
from dataclasses import fields
from json import dumps, loads
from typing import Any, Dict

from app.core.helpers.strings import to_dict_camel_case, to_dict_snake_case


class BaseCollection:

    def to_dict(self) -> Dict:
        return loads(dumps(self, default=lambda formated: to_dict_camel_case(formated.__dict__)))

    def collection(self) -> str:
        return self.__class__.__name__

    @staticmethod
    def class_from_dict(class_name: Any, dict: Dict):
        dict = to_dict_snake_case(dict)
        field_set = {f.name for f in fields(class_name) if f.init}
        filtered_arg_dict = {key: value for key,
                             value in dict.items() if key in field_set}
        return class_name(**filtered_arg_dict)
