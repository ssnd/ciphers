from ciphers.cipher import Cipher


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
        key = self.key
        encrypted_string = ""
        for index, char in enumerate(text):
            xored_char = ord(char) ^ ord(key[index % len(key)])
            encrypted_string += chr(xored_char)
        return repr(encrypted_string)

    def decrypt(self, text: str) -> str:
        key = self.key
        text = eval(text)
        decrypted_string = ""
        for index, char in enumerate(text):
            xored_char = ord(char) ^ ord(key[index % len(key)])
            decrypted_string += chr(xored_char)

        return decrypted_string
