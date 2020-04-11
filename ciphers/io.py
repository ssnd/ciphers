import click
import io
from dataclasses import dataclass


@dataclass
class IOHandler:
    input_file: io.TextIOWrapper
    output_file: click.utils.LazyFile

    def read(self) -> str:
        if self.input_file is None:
            return self.prompt()
        return self.read_file()

    def prompt(self) -> str:
        value = click.prompt('Enter the text to be encoded', type=str)
        return value

    def read_file(self) -> str:
        value = self.input_file.read()
        self.input_file.close()

        return value

    def write(self, text: str) -> None:
        if self.output_file is None:
            return self.echo(text)
        return self.write_file(text)

    def echo(self, text: str) -> None:
        click.echo("Encrypted text: " + text)

    def write_file(self, text: str) -> None:
        f = self.output_file.open()
        f.write(text)
        f.close()
