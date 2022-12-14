
from time import time

import jwt

from app.core.collections import Auth, Token
from app.core.helpers.constants import ISS, TOKEN_EXPIRES_IN
from app.core.helpers.strings import to_dict_snake_case
from app.ports.external import JwtPort


class JwtAdapter(JwtPort):

    def encode_bearer(self, auth: Auth, ispb: str, key: str) -> str:
        now = int(time())
        token = Token(
            exp=now + TOKEN_EXPIRES_IN,
            iat=now,
            ispb=ispb,
            iss=ISS,
            user_id=auth.id
        ).to_dict()

        return str(jwt.encode(token, key, algorithm='HS256'))

    def decode_bearer(self, bearer: str, key: str) -> Token:
        def prepare_key(key):
            return jwt.utils.force_bytes(key)
        jwt.api_jws._jws_global_obj._algorithms['HS256'].prepare_key = prepare_key
        dict_token = to_dict_snake_case(
            jwt.decode(bearer, key, algorithms=['HS256']))
        return Token(**dict_token)
