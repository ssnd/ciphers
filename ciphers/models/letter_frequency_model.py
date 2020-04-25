from dataclasses import dataclass
from ciphers.models.model import Model
import sys


@dataclass
class LetterFrequencyModel(Model):
    alphabet: str = ("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
                     "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
                     "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
                     "1234567890!\"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ ")

    def model_function(self, text: str) -> object:
        """Count the frequency of each letter in the given string.

        Arguments:
            text {str} -- input text

        Returns:
            object -- an object containing each letter and it's frequency.
        """
        alphabet = list(set(self.alphabet))

        if len(text) == 0:
            print("The input text is empty. Exitting...")
            sys.exit()

        return {x: text.count(x) / len(text)
                for x in alphabet}
