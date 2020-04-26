import pytest
from ciphers.vigenere import Vigenere


testdata = [
    "AbC, bcd?",
    "АбВ, ГДЕёжхияй?",
    "abc\n\nπø¨¥®\nbcd",
]


@pytest.mark.parametrize("a", testdata)
def test_vigenere_algorithm_enc_dec(a):
    c = Vigenere(key="42")
    assert c.decrypt(c.encrypt(a)) == a


@pytest.mark.parametrize("a", testdata)
def test_vigenere_algorithm_dec_enc(a):
    c = Vigenere(key="42")
    assert c.encrypt(c.decrypt(a)) == a


def test_vigenere_algorithm_enc():
    c = Vigenere(key="42")
    assert c.encrypt("abc\n") == "436\n"


def test_vigenere_algorithm_dec():
    c = Vigenere(key="42")
    assert c.decrypt("bcdø") == "PSRø"
