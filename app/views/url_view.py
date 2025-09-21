from sqlalchemy.orm import Session

from app.config import get_settings
from app.db.repository import UrlRepository
from app.models.url import ShortenIn, ShortenOut
from app.services.shortener import ShortenerService
from app.validators.url_validator import validate_url


def shorten_url(payload: ShortenIn, session: Session) -> ShortenOut:
    # validation
    valid_url = validate_url(payload.url.unicode_string())

    # db
    repo = UrlRepository(session)

    # business logic
    service = ShortenerService(repo)
    code = service.shorten(valid_url)

    session.commit()
    session.refresh(repo.get_by_code(code))

    base = str(get_settings().base_url).rstrip("/")
    return ShortenOut(short_url=f"{base}/r/{code}")


def resolve_url(code: str, session: Session) -> str:
    repo = UrlRepository(session)
    service = ShortenerService(repo)
    return service.resolve(code)
