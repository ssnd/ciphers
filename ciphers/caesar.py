from ciphers.cipher import Cipher


class Caesar(Cipher):
    key: int

    def encrypt(self, text: str) -> str:
        """Encrypt using caesar cipher

        Arguments:
            text {str} -- input string

        Returns:
            str -- encrypted string
        """

        encrypted_string = ""
        for index, char in enumerate(text):
            if char not in self.alphabet:
                encrypted_string += char
                continue

            index = (self.alphabet.index(char) + self.key) % len(self.alphabet)
            encrypted_string += self.alphabet[index]

        return encrypted_string

    def decrypt(self, text: str) -> str:
        """Decrypt using caesar cipher

        Arguments:
            text {str} -- input string

        Returns:
            str -- decrypted string
        """
        decrypted_string = ""
        for index, char in enumerate(text):
            if char not in self.alphabet:
                decrypted_string += char
                continue

            index = (self.alphabet.index(char) - self.key) % len(self.alphabet)
            decrypted_string += self.alphabet[index]

        return decrypted_string
