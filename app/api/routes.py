from fastapi import APIRouter, Depends
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session

from app.db.session import get_session
from app.models.url import ShortenIn, ShortenOut
from app.views import url_view

router = APIRouter()


@router.post("/shorten", response_model=ShortenOut)
def create_short_url(
        payload: ShortenIn,
        db: Session = Depends(get_session),
):
    return url_view.shorten_url(payload, db)


@router.get("/r/{code}")
def redirect(code: str, db: Session = Depends(get_session)):
    url = url_view.resolve_url(code, db)
    return RedirectResponse(url)
