import pytest
from ciphers.caesar import Caesar

testdata = [
    "AbC, bcd?",
    "АбВ, ГДЕёжхияй?",
    "abc\n\nπø¨¥®\nbcd",
]


@pytest.mark.parametrize("a", testdata)
def test_caesar_algorithm_enc_dec(a):
    c = Caesar(key=42)
    assert c.decrypt(c.encrypt(a)) == a


@pytest.mark.parametrize("a", testdata)
def test_caesar_algorithm_dec_enc(a):
    c = Caesar(key=42)
    assert c.encrypt(c.decrypt(a)) == a


def test_caesar_algorithm_enc():
    c = Caesar(key=1)
    assert c.encrypt("abc\n") == "bcd\n"


def test_caesar_algorithm_dec():
    c = Caesar(key=1)
    assert c.decrypt("bcdø") == "abcø"
