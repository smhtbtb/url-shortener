import re

from app.utils.exceptions import BadRequest

URL_REGEX = re.compile(
    r"^(https?://)"
    r"(([A-Za-z0-9-]+\.)+[A-Za-z]{2,})"
    r"(:\d+)?(/.*)?$"
)


def validate_url(url: str) -> str:
    """Raise BadRequest if url is not valid"""
    if not URL_REGEX.match(url):
        raise BadRequest("Invalid URL format: must start with http:// or https://")
    return url
