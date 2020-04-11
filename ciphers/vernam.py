from ciphers.cipher import Cipher
import sys


class Vernam(Cipher):
    key: str
    """Vernam Cipher encryption/decryption class
    """

    def encrypt(self, text: str) -> str:
        """Encrypt the input text using the Vernam cipher

        Arguments:
            text {str} -- input text

        Returns:
            str -- the encrypted text
        """
        alph = self.alphabet
        key = self.prep_key(text)
        encrypted_string = ""
        for index, char in enumerate(text):
            if char not in alph:
                encrypted_string += char + " "
                continue

            new_index = alph.index(char) ^ alph.index(key[index])
            encrypted_string += hex(new_index) + " "

        return encrypted_string[:-1]

    def decrypt(self, text: str) -> str:
        """Decrypt the text using the Vernam cipher

        Arguments:
            text {str} -- the text to be decrypted

        Returns:
            str -- the decrypted text
        """
        alph = self.alphabet
        key = self.prep_key(text)
        decrypted_string = []

        splitted_text = text.split(" ")
        print(splitted_text)
        encrypted_integers = []

        for el in splitted_text:
            if el[:2] == '0x':
                encrypted_integers.append(int(el, 0))
            else:
                encrypted_integers.append(ord(el) + sys.maxsize)

        for i, integer in enumerate(encrypted_integers):
            if (integer >= sys.maxsize):
                decrypted_string.append(chr(integer-sys.maxsize))
                continue

            new_index = integer ^ alph.index(key[i])
            decrypted_string.append(alph[new_index])

        return "".join(decrypted_string)
