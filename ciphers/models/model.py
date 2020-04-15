from dataclasses import dataclass
import json
from ciphers.io_handler import IOHandler
from typing import Union, Dict, Any
import abc


@dataclass  # type: ignore
class Model(abc.ABC):
    """Generic model abstract class.
    """
    model: Union[object, None] = None

    def train_model(self,
                    output_file_path: Union[str, None] = None,
                    input_file_path: Union[str, None] = None) -> Dict:
        """Train the model

        Keyword Arguments:
            output_file_path {Union[str, None]} -- file to save the model to.
            (default: {None})
            input_file_path {Union[str, None]} -- file to read the model form.
            (default: {None})

        Returns:
            Dict -- the model dictionary.
        """
        io = IOHandler(input_file=input_file_path,
                       output_file=output_file_path)
        text = io.read()
        trained_frequencies = self.model_function(text)
        self.model = trained_frequencies
        dump = json.dumps(trained_frequencies)
        io.write(dump)

        return trained_frequencies

    def get_trained_model(self, file_path: str) -> object:
        """Load the model from a provided path.

        Arguments:
            file_path {str} -- the path of the model

        Returns:
            object -- The model object itself.
        """
        io = IOHandler(input_file=file_path)
        raw_json_model = io.read()
        self.model = json.loads(raw_json_model)

        return self.model

    @abc.abstractmethod
    def model_function(self, text) -> Any:
        """The virtual model function to be overloaded.
        """
        pass
