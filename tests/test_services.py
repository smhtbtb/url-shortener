def test_shorten_and_resolve(service):
    code = service.shorten("https://example.com/x")
    assert len(code) == 5
    assert service.resolve(code) == "https://example.com/x"


def test_idempotency(service):
    url = "https://example.com/a"
    code1 = service.shorten(url)
    code2 = service.shorten(url)  # idempotent
    assert code1 == code2
