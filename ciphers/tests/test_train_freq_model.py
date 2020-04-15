import json
from ciphers.models.letter_frequency_model import LetterFrequencyModel


def test_model_train_from_file(tmp_path):
    d = tmp_path / "sub"
    d.mkdir()
    input_p = d / "input.json"
    input_p.write_text("abcde")
    model_p = d / "model.json"
    m = LetterFrequencyModel(alphabet="abcde")
    m.train_model(input_file_path=input_p, output_file_path=model_p)
    trained_dict = {"a": 0.2,
                    "b": 0.2,
                    "c": 0.2,
                    "d": 0.2,
                    "e": 0.2}

    output_contents = model_p.read_text()
    output_json = json.loads(output_contents)
    json_from_file = m.get_trained_model(model_p)
    assert trained_dict == output_json
    assert json_from_file == trained_dict
    assert input_p.read_text() == "abcde"
