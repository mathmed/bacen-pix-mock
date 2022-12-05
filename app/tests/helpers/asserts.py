from typing import Dict
from unittest import TestCase

from app.core.helpers.http import HttpError
from app.core.helpers.strings import to_dict_camel_case


def assert_http_error(function, status_code: int, *args):
    with TestCase().assertRaises(HttpError) as e:
        if args:
            function(args)()
        else:
            function()()
    assert e.exception.status_code == status_code


def assert_dict_and_objects(object1: object | Dict, object2: object | Dict):

    if not isinstance(object1, dict):
        object1 = to_dict_camel_case(object1.__dict__)

    if not isinstance(object2, dict):
        object2 = to_dict_camel_case(object2.__dict__)

    for key in object1.keys():
        assert object1[key] == object2[key]
