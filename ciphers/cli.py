import click
from ciphers.caesar import Caesar
from ciphers.vigenere import Vigenere
from ciphers.vernam import Vernam
from ciphers.io_handler import IOHandler
from ciphers.hack_caesar import HackCaesar
from typing import Union
import sys


@click.group()
def cli(): pass


@cli.command()
@click.option("-c", "--cipher",
              required=True,
              type=click.Choice(['caesar', 'vigenere', 'vernam']),
              help="Cipher type: Caesar, Vigenere or Vernam")
@click.option("-k", "--key",
              type=click.STRING,
              required=True,
              help=("The key: integer for Caesar, "
                    "string for Vigenere and Vernam."))
@click.option("--input-file",
              default=None,
              type=click.File(),
              help="The input file to read the text from.")
@click.option("--output-file",
              default=None,
              type=click.File("w"),
              help="Output file to write the text to.")
def encode(cipher: str, key: Union[int, str], input_file, output_file):
    """Use this command to encode the text (read from stdio or a file)
       using the available ciphers and display the encrypted text or write
       it to a file.
    """
    input_path = input_file.name if input_file is not None else None
    output_path = output_file.name if output_file is not None else None

    io_handler = IOHandler(input_path, output_path)

    input_text = io_handler.read()

    if cipher == "caesar":
        key = Caesar.check_key_type(key, int)
        c = Caesar(key=key)
        encrypted_str = c.encrypt(input_text)

    if cipher == "vigenere":
        vigenere = Vigenere(key=key)
        encrypted_str = vigenere.encrypt(input_text)

    if cipher == "vernam":
        if output_file is None:
            print(("An output file is required for the Vernam cipher"
                   " to work correctly. Exitting..."))
            sys.exit()
        vernam = Vernam(key=key)
        encrypted_str = vernam.encrypt(input_text)

    io_handler.write(encrypted_str)


@cli.command()
@click.option("-c", "--cipher",
              required=True,
              type=click.Choice(['caesar', 'vigenere', 'vernam']),
              help="Cipher type: Caesar, Vigenere or Vernam")
@click.option("-k", "--key",
              type=click.STRING,
              required=True,
              help=("The key: integer for Caesar, "
                    "string for Vigenere and Vernam."))
@click.option("--input-file",
              default=None,
              type=click.File(),
              help="The input file to read the text from.")
@click.option("--output-file",
              default=None,
              type=click.File("w"),
              help="Output file to write the text to.")
def decode(cipher: str, key: Union[int, str], input_file, output_file):
    """Use this command to decode the text (read from stdio or a file)
       using the available ciphers and display the decrypted text or write
       it to a file.
    """

    input_file_name = input_file.name if input_file is not None else None
    output_file_name = output_file.name if output_file is not None else None

    io_handler = IOHandler(input_file_name, output_file_name)

    input_text = io_handler.read()

    if cipher == "caesar":
        key = Caesar.check_key_type(key, int)
        c = Caesar(key=key)
        decrypted_str = c.decrypt(input_text)

    if cipher == "vigenere":
        v = Vigenere(key=key)
        decrypted_str = v.decrypt(input_text)

    if cipher == "vernam":
        if input_file is None:
            print(("An input file is required for the Vernam cipher"
                   " to work correctly. Exitting..."))
            sys.exit()
        vernam = Vernam(key=key)
        decrypted_str = vernam.decrypt(input_text)

    io_handler.write(decrypted_str)


@cli.command()
@click.option("--input-file",
              default=None,
              type=click.File(),
              help="The input file to read the text from.")
@click.option("--output-file",
              default=None,
              type=click.File("w"),
              help="Output file to write the text to.")
@click.option("--model-file",
              default=None,
              required=True,
              type=click.File(),
              help="The model file to use.")
def hack(input_file, output_file, model_file):
    """Use this tool to try to guess the key for the input text.
    """
    input_path = input_file.name if input_file is not None else None
    output_path = output_file.name if output_file is not None else None
    model_path = model_file.name if model_file is not None else None

    io_handler = IOHandler(input_path, output_path)

    input_text = io_handler.read()

    h = HackCaesar()

    h.get_model(model_path)
    decrypted = h.hack(input_text)

    io_handler.write(decrypted, display_text="The hacked text is: ")
