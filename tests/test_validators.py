import pytest

from app.utils.exceptions import BadRequest
from app.validators.url_validator import validate_url


def test_valid_http_url():
    url = "http://example.com"
    assert validate_url(url) == url


def test_valid_https_url():
    url = "https://example.com/path"
    assert validate_url(url) == url


def test_url_with_port_and_path():
    url = "http://example.com:8080/test/path"
    assert validate_url(url) == url


def test_invalid_url_no_scheme():
    with pytest.raises(BadRequest) as exc:
        validate_url("example.com")
    assert "Invalid URL format" in str(exc.value.detail)


def test_invalid_url_wrong_scheme():
    with pytest.raises(BadRequest) as exc:
        validate_url("ftp://example.com")
    assert "Invalid URL format" in str(exc.value.detail)
