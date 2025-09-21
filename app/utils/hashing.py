import hashlib

ALPHABET = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
BASE = len(ALPHABET)


def base62_encode(num: int) -> str:
    if num == 0:
        return ALPHABET[0]
    chars = []
    while num > 0:
        num, rem = divmod(num, BASE)
        chars.append(ALPHABET[rem])
    return "".join(reversed(chars))


def short_code_for(url: str, length: int = 5, salt: str = "") -> str:
    digest = hashlib.sha256((salt + url).encode()).digest()
    num = int.from_bytes(digest[:8], "big", signed=False)
    code = base62_encode(num)[:length]
    return code.ljust(length, ALPHABET[0])
