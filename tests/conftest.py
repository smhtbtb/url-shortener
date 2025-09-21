import pytest

from app.db.repository import UrlRepository
from app.services.shortener import ShortenerService


class InMemoryRepo(UrlRepository):
    def __init__(self):
        self._store = {}
        self._reverse = {}

    def create(self, short_code: str, long_url: str):
        self._store[short_code] = long_url
        self._reverse[long_url] = short_code

    def get_by_code(self, short_code: str):
        v = self._store.get(short_code)
        return type("Obj", (), {"short_code": short_code, "long_url": v}) if v else None

    def get_by_url(self, long_url: str):
        c = self._reverse.get(long_url)
        return type("Obj", (), {"short_code": c, "long_url": long_url}) if c else None


@pytest.fixture
def repo():
    return InMemoryRepo()


@pytest.fixture
def service(repo):
    return ShortenerService(repo)
