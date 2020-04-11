from ciphers.caesar import Caesar
from random import randint


def test_caesar_algorithm():
    c = Caesar(key=randint(1, 4000))
    assert c.decrypt(c.encrypt("AbC, bcd?")) == "AbC, bcd?"


def test_caesar_algorithm_cyrillic():
    c = Caesar(key=randint(1, 4000))
    assert c.decrypt(c.encrypt("АбВ, ГДЕёжхияй?")) == "АбВ, ГДЕёжхияй?"


def test_encrypt_caesar_nospace():
    c = Caesar(key=randint(1, 4000))
    assert c.decrypt(c.encrypt("abc")) == "abc"


def test_encrypt_caesar_spaces():
    c = Caesar(key=randint(1, 4000))
    assert c.decrypt(c.encrypt("abc bcd")) == "abc bcd"


def test_encrypt_caesar_chars_upper():
    c = Caesar(key=randint(1, 4000))
    assert c.decrypt(c.encrypt("AbC, bcd?")) == "AbC, bcd?"


def test_decrypt_caesar_nospace():
    c = Caesar(key=randint(1, 4000))
    assert c.encrypt(c.decrypt("bcd")) == "bcd"


def test_decrypt_caesar_spaces():
    c = Caesar(key=randint(1, 4000))
    assert c.encrypt(c.decrypt("bcd cde")) == "bcd cde"


def test_decrypt_caesar_chars_upper():
    c = Caesar(key=randint(1, 4000))
    assert c.encrypt(c.decrypt("BcD, cde?")) == "BcD, cde?"


def test_encrypt_caesar_cyrillic():
    c = Caesar(key=1)
    assert c.encrypt(c.decrypt("АБВ, где?")) == "АБВ, где?"
