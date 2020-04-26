from dataclasses import dataclass, field
from ciphers.models.letter_frequency_model import LetterFrequencyModel
from ciphers.caesar import Caesar
from typing import Union, Dict
import sys


@dataclass
class HackCaesar():
    """Use letter frequencies to hack the cipher
    """
    model: Union[Dict, None] = None
    model_instance: LetterFrequencyModel =\
        field(default_factory=LetterFrequencyModel)

    def get_model(self, path: str):
        """Load the model.

        Arguments:
            path {str} -- the path to the model file
        """
        self.model = self.model_instance.get_trained_model(file_path=path)

    def check_input_data(self, encrypted: str) -> bool:
        """Run the checks to be sure that this model fits
        the provided data. This method tests the input text length.

        Arguments:
            encrypted {str} -- encrypted text

        Returns:
            bool -- whether the text should be analyzed using this method.
        """
        if len(encrypted) < 10:
            print("The input text is too short. Exitting...")
            sys.exit()

        return True

    def hack(self, encrypted: str) -> Union[str, None]:
        """Guess the key by finding the one with the minimal
        MSE wrt to the letter frequencies in the model.

        Arguments:
            encrypted {str} -- encrypted text

        Returns:
            Union[str, None] -- Decrypted text, or None if the decryption
            is impossible for some reason.
        """
        if self.model is None:
            print("No model provided. Exitting...")
            sys.exit()

        if not self.check_input_data(encrypted):
            return None

        mse = self.mse
        trained = self.model
        freqs_dict = self.model_instance.model_function
        alphabet = self.model_instance.alphabet

        errors = []
        for key in range(len(alphabet)):
            c1 = Caesar(key=key)
            try_freqs = freqs_dict(c1.decrypt(encrypted))
            errors.append(sum([mse(trained[l], try_freqs[l])
                               for l in alphabet]))

        min_error = min(errors)
        key = errors.index(min_error)
        c2 = Caesar(key=key)
        decrypted = c2.decrypt(encrypted)
        return decrypted

    @staticmethod
    def mse(x: float, y: float) -> float:
        """Mean squared error

        Arguments:
            x {float} -- x
            y {float} -- y

        Returns:
            float -- result
        """
        return (x - y) ** 2
