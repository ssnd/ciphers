from dataclasses import dataclass
from typing import Union


@dataclass
class Cipher:
    """Abstract Cipher class to be used to define different kinds of ciphers.
    """
    key: Union[str, int]
    alphabet: str = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJK\
LMNOPQRSTUVWXYZабвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМН\
ОПРСТУФХЦЧШЩЪЫЬЭЮЯ1234567890!\"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ "

    def encrypt(self, text: str) -> str:
        pass

    def decrypt(self, text: str) -> str:
        pass

    def prep_key(self, text: str) -> str:
        """The length of the key in this cipher should be equal to the length
        of the text that has to be encrypted. This function makes sure
        these lengths are equal.

        Arguments:
            text {str} -- the key text

        Returns:
            str -- the key of the length needed
        """
        key = str(self.key)
        dict_key = [key[i % len(key)]
                    for i in range(len(text))]

        return "".join(dict_key)

    @staticmethod
    def check_key_type(key: Union[str, int], key_type: type) \
            -> Union[str, int]:
        """Check if the provided key has the correct type.
        Useful in Caesar cipher where the key should be integer.

        Raises:
            ValueError: if the type of the key isn't correct

        Returns:
            [str or int] -- the key itself.
        """
        try:
            key = key_type(key)
        except ValueError:
            raise ValueError("The key should be of type {}."
                             .format(key_type.__name__))

        return key
