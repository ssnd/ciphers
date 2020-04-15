from dataclasses import dataclass
from ciphers.models.model import Model


@dataclass
class LetterFrequencyModel(Model):
    alphabet: str = ("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
                     "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
                     "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
                     "1234567890!\"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ ")

    def model_function(self, text: str) -> object:
        alphabet = list(set(self.alphabet))

        return {x: text.count(x) / len(text)
                for x in alphabet}
