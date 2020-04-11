from ciphers.vigenere import Vigenere
from random import choice


def random_string(stringLength=10):
    """Generate a random string of fixed length """
    letters = Vigenere.alphabet
    return ''.join(choice(letters) for i in range(stringLength))


def test_vigenere_algorithm():
    c = Vigenere(key=random_string())
    assert c.decrypt(c.encrypt("AbC, bcd?")) == "AbC, bcd?"


def test_vigenere_algorithm_cyrillic():
    c = Vigenere(key=random_string())
    assert c.decrypt(c.encrypt("АбВ, ГДЕёжхияй?")) == "АбВ, ГДЕёжхияй?"


def test_encrypt_vigenere_nospace():
    c = Vigenere(key=random_string())
    assert c.decrypt(c.encrypt("abc")) == "abc"


def test_encrypt_vigenere_spaces():
    c = Vigenere(key=random_string())
    assert c.decrypt(c.encrypt("abc bcd")) == "abc bcd"


def test_encrypt_vigenere_chars_upper():
    c = Vigenere(key=random_string())
    assert c.decrypt(c.encrypt("AbC, bcd?")) == "AbC, bcd?"


def test_decrypt_vigenere_nospace():
    c = Vigenere(key=random_string())
    assert c.encrypt(c.decrypt("bcd")) == "bcd"


def test_decrypt_vigenere_spaces():
    c = Vigenere(key=random_string())
    assert c.encrypt(c.decrypt("bcd cde")) == "bcd cde"


def test_decrypt_vigenere_chars_upper():
    c = Vigenere(key=random_string())
    assert c.encrypt(c.decrypt("BcD, cde?")) == "BcD, cde?"


def test_encrypt_vigenere_cyrillic():
    c = Vigenere(key=random_string())
    assert c.encrypt(c.decrypt("АБВ, где?")) == "АБВ, где?"
