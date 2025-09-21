from datetime import datetime, timezone

from sqlalchemy import String, UniqueConstraint, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from app.db.session import Base


class UrlMap(Base):
    __tablename__ = "url_map"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    short_code: Mapped[str] = mapped_column(String(8), nullable=False)
    long_url: Mapped[str] = mapped_column(String(2048), nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        nullable=False
    )
    __table_args__ = (
        UniqueConstraint("short_code", name="uq_short_code"),
    )


from pydantic import BaseModel, AnyUrl


class ShortenIn(BaseModel):
    url: AnyUrl


class ShortenOut(BaseModel):
    short_url: AnyUrl
