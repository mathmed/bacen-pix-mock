from passlib.hash import pbkdf2_sha256

from app.ports.external import EncryptPort


class Passlib(EncryptPort):

    def encrypt(self, password: str) -> str:
        return pbkdf2_sha256.hash(password)

    def verify(self, encrypted: str, password: str) -> bool:
        return pbkdf2_sha256.verify(password, encrypted)
