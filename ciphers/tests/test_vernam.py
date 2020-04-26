import pytest
from ciphers.vernam import Vernam


testdata: list = [
    "AbC, bcd?",
    "АбВ, ГДЕёжхияй?",
    "abc\n\n\nbcd",
]


@pytest.mark.parametrize("a", testdata)
def test_vernam_algorithm_enc_dec(a):
    c = Vernam(key="keytest")
    assert c.decrypt(c.encrypt(a)) == a
