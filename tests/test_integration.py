import os

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.db.session import Base, get_session
from app.main import app

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)


def override_get_session():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


app.dependency_overrides[get_session] = override_get_session
client = TestClient(app)


def test_shorten_and_redirect():
    url = "https://example.com"
    resp = client.post("/shorten", json={"url": url})
    assert resp.status_code == 200
    short_url = resp.json()["short_url"]

    code = short_url.split("/")[-1]
    resp2 = client.get(f"/r/{code}", follow_redirects=False)
    assert resp2.status_code == 307
    assert resp2.headers["location"].rstrip("/") == url


@pytest.fixture(scope="session", autouse=True)
def cleanup_db():
    yield
    if os.path.exists("test.db"):
        os.remove("test.db")
