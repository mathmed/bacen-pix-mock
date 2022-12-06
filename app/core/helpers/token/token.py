from contextvars import ContextVar

from app.core.collections import Token

TOKEN: ContextVar[Token] = ContextVar('TOKEN', default=None)


def get_token() -> Token:
    return TOKEN.get()


def set_token(new_token: Token):
    TOKEN.set(new_token)
