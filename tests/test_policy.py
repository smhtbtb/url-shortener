from app.services.shortener import ShortCodePolicy


def test_clamp_truncate():
    policy = ShortCodePolicy(max_len=6)
    assert policy.clamp("ABCDEFG") == "ABCDEF"


def test_clamp_pad():
    policy = ShortCodePolicy(max_len=6)
    assert policy.clamp("AB") == "ABaaaa"
