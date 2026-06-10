from twttr import shorten

def test_numbers():
    assert shorten("1234") == "1234"


def test_cases():
    assert shorten("twitter") == "twttr"
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("HELLOméd") == "HLLméd"


def test_punctuation():
    assert shorten("hello, world!") == "hll, wrld!"
