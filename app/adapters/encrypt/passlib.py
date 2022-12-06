from passlib.hash import pbkdf2_sha256


def encrypt(password: str) -> str:
    return pbkdf2_sha256.hash(password)


def verify(encrypted: str, password: str) -> bool:
    return pbkdf2_sha256.verify(password, encrypted)
