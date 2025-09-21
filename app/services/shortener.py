from dataclasses import dataclass
from typing import Optional

from app.config import get_settings
from app.db.repository import UrlRepository
from app.utils.exceptions import NotFound, Conflict
from app.utils.hashing import short_code_for


@dataclass(frozen=True)
class ShortCodePolicy:
    max_len: int

    def clamp(self, code: str) -> str:
        if len(code) > self.max_len:
            return code[: self.max_len]
        if len(code) < self.max_len:
            from app.utils.hashing import ALPHABET
            return code.ljust(self.max_len, ALPHABET[0])
        return code


class ShortenerService:
    def __init__(self, repo: UrlRepository, policy: Optional[ShortCodePolicy] = None):
        self.repo = repo
        self.policy = policy or ShortCodePolicy(max_len=get_settings().max_code_len)

    def shorten(self, long_url: str) -> str:
        existing = self.repo.get_by_url(long_url)
        if existing:
            return existing.short_code

        code = self.policy.clamp(short_code_for(long_url, length=self.policy.max_len))
        salt_i = 0
        while self.repo.get_by_code(code) is not None:
            salt_i += 1
            code = self.policy.clamp(short_code_for(long_url, length=self.policy.max_len, salt=str(salt_i)))
            if salt_i > 10:
                raise Conflict("Too many collisions, try later")
        self.repo.create(short_code=code, long_url=long_url)
        return code

    def resolve(self, short_code: str) -> str:
        obj = self.repo.get_by_code(short_code)
        if not obj:
            raise NotFound("Short code not found")
        return obj.long_url
