from functools import lru_cache
from pydantic import BaseModel, AnyUrl
import os

class Settings(BaseModel):
    app_host: str = os.getenv("APP_HOST", "0.0.0.0")
    app_port: int = int(os.getenv("APP_PORT", 8000))
    database_url: str = os.getenv("DATABASE_URL", "sqlite+pysqlite:///:memory:")
    base_url: AnyUrl = os.getenv("BASE_URL", "http://localhost:8000")
    max_code_len: int = 5

@lru_cache
def get_settings() -> Settings:
    return Settings()
