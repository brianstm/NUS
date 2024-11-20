from twttr import shorten


def test_no_vowels():
    assert shorten("hello") == "hll"
    assert shorten("world") == "wrld"


def test_uppercase():
    assert shorten("HELLO") == "HLL"
    assert shorten("TWITTER") == "TWTTR"


def test_mixed_case():
    assert shorten("HeLLo WoRLd") == "HLL WRLd"


def test_empty_string():
    assert shorten("") == ""


def test_numbers_and_symbols():
    assert shorten("1234!@#$") == "1234!@#$"
    assert shorten("AEIOU123") == "123"
