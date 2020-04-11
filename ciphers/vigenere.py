from ciphers.cipher import Cipher


class Vigenere(Cipher):
    """Vigenere Cipher encryption/decryption class
    """
    key: str

    def encrypt(self, text: str) -> str:
        """Encrypt the input text using the Vigenere cipher

        Arguments:
            text {str} -- input text

        Returns:
            str -- the encrypted text
        """
        alph = self.alphabet
        key = self.prep_key(text)
        print(text, key)
        encrypted_string = ""
        for index, char in enumerate(text):
            new_index = (alph.index(char) + alph.index(key[index])) % len(alph)
            encrypted_string += alph[new_index]

        return encrypted_string

    def decrypt(self, text: str) -> str:
        """Decrypt the text using the Vigenere cipher

        Arguments:
            text {str} -- the text to be decrypted

        Returns:
            str -- the decrypted text
        """
        alph = self.alphabet
        key = self.prep_key(text)
        decrypted_string = ""
        for index, char in enumerate(text):
            new_index = (alph.index(char) - alph.index(key[index])) % len(alph)
            decrypted_string += alph[new_index]

        return decrypted_string
