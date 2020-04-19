from ciphers.models.letter_frequency_model import LetterFrequencyModel
import os


def test_model_train_from_file(tmp_path):
    d = tmp_path / "sub"
    d.mkdir()
    model_p = d / "model.json"
    m = LetterFrequencyModel(alphabet="abcde")
    input_file_path = os.getcwd() + "/ciphers/tests/static/input.txt"
    model_dict = m.train_model(input_file_path=input_file_path,
                               output_file_path=model_p)
    trained_dict = {"a": 0.2,
                    "b": 0.2,
                    "c": 0.2,
                    "d": 0.2,
                    "e": 0.2}

    assert trained_dict == model_dict
