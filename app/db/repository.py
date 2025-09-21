from typing import Optional
from sqlalchemy.orm import Session
from sqlalchemy import select
from app.models.url import UrlMap

class UrlRepository:
    def __init__(self, session: Session):
        self.session = session

    def create(self, short_code: str, long_url: str) -> UrlMap:
        obj = UrlMap(short_code=short_code, long_url=long_url)
        self.session.add(obj)
        return obj

    def get_by_code(self, short_code: str) -> Optional[UrlMap]:
        stmt = select(UrlMap).where(UrlMap.short_code == short_code)
        return self.session.execute(stmt).scalar_one_or_none()

    def get_by_url(self, long_url: str) -> Optional[UrlMap]:
        stmt = select(UrlMap).where(UrlMap.long_url == long_url)
        return self.session.execute(stmt).scalar_one_or_none()
