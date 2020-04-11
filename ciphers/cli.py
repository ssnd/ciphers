import click
from ciphers.caesar import Caesar
from ciphers.vigenere import Vigenere
from ciphers.vernam import Vernam
from ciphers.io import IOHandler
from typing import Union


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
              help="The key: integer for Caesar, string for" +
                   "Cigenere and Vernam.")
@click.option("--input-file",
              default=None,
              type=click.File(),
              help="The input file to read the text from.")
@click.option("--output-file",
              default=None,
              type=click.File("w"),
              help="Output file to write the text to.")
def encode(cipher: str, key: Union[int, str], input_file, output_file):
    """encode docstring
    """

    io_handler = IOHandler(input_file, output_file)

    input_text = io_handler.read()

    if cipher == "caesar":
        key = Caesar.check_key_type(key, int)
        c = Caesar(key=key)
        encrypted_str = c.encrypt(input_text)

    if cipher == "vigenere":
        vigenere = Vigenere(key=key)
        encrypted_str = vigenere.encrypt(input_text)

    if cipher == "vernam":
        vernam = Vernam(key=key)
        encrypted_str = vernam.encrypt(input_text)

    io_handler.write(encrypted_str)


@cli.command()
@click.option("-c", "--cipher",
              required=True,
              type=click.Choice(['caesar', 'vigenere', 'vernam']),
              help="Cipher type: Caesar, vigenere or Vernam")
@click.option("-k", "--key",
              type=click.STRING,
              required=True,
              help="The key: integer for Caesar, string for" +
                   "Cigenere and Vernam.")
@click.option("--input-file",
              default=None,
              type=click.File(),
              help="The input file to read the text from.")
@click.option("--output-file",
              default=None,
              type=click.File("w"),
              help="Output file to write the text to.")
def decode(cipher: str, key: Union[int, str], input_file, output_file):
    """decode docstring
    """

    io_handler = IOHandler(input_file, output_file)

    input_text = io_handler.read()

    if cipher == "caesar":
        key = Caesar.check_key_type(key, int)
        c = Caesar(key=key)
        decrypted_str = c.decrypt(input_text)

    if cipher == "vigenere":
        v = Vigenere(key=key)
        decrypted_str = v.decrypt(input_text)

    if cipher == "vernam":
        vernam = Vernam(key=key)
        decrypted_str = vernam.decrypt(input_text)

    io_handler.write(decrypted_str)


@cli.command()
def hack():
    """hack docstring
    """
    click.echo('hack')
