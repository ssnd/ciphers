from ciphers.vernam import Vernam
from random import choice


def random_string(stringLength=10):
    """Generate a random string of fixed length """
    letters = Vernam.alphabet
    return ''.join(choice(letters) for i in range(stringLength))


def test_vernam_algorithm():
    c = Vernam(key=random_string())
    assert c.decrypt(c.encrypt("AbC, bcd?")) == "AbC, bcd?"


def test_vernam_algorithm_cyrillic():
    c = Vernam(key=random_string())
    assert c.decrypt(c.encrypt("АбВ, ГДЕёжхияй?")) == "АбВ, ГДЕёжхияй?"


def test_encrypt_vernam_nospace():
    c = Vernam(key=random_string())
    assert c.decrypt(c.encrypt("abc")) == "abc"


def test_encrypt_vernam_spaces():
    c = Vernam(key=random_string())
    assert c.decrypt(c.encrypt("abc bcd")) == "abc bcd"


def test_encrypt_vernam_chars_upper():
    c = Vernam(key=random_string())
    assert c.decrypt(c.encrypt("AbC, bcd?")) == "AbC, bcd?"


def test_decrypt_vernam_nospace():
    c = Vernam(key=random_string())
    assert c.decrypt(c.encrypt("bcd")) == "bcd"


def test_decrypt_vernam_spaces():
    c = Vernam(key=random_string())
    assert c.decrypt(c.encrypt("bcd cde")) == "bcd cde"


def test_decrypt_vernam_chars_upper():
    c = Vernam(key=random_string())
    assert c.decrypt(c.encrypt("BcD, cde?")) == "BcD, cde?"


def test_encrypt_vernam_cyrillic():
    c = Vernam(key=random_string())
    assert c.decrypt(c.encrypt("АБВ, где?")) == "АБВ, где?"
