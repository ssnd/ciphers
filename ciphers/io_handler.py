import click
from dataclasses import dataclass
from typing import Any


@dataclass
class IOHandler:
    input_file: Any = None
    output_file: Any = None

    def read(self) -> str:
        """Read the text from the stdin or the input file.

        Returns:
            str -- the file contents
        """
        if self.input_file is None:
            return self.prompt()
        return self.read_file()

    def prompt(self, display_text: str = "Enter the input text") -> str:
        """Use the stdin to get the info

        Keyword Arguments:
            display_text {str} -- The default text before the user input
             (default: {"Enter the input text"})

        Returns:
            str -- the text from the stdin.
        """

        value = click.prompt(display_text, type=str)
        return value

    def read_file(self) -> str:
        """Read the file from the given path.

        Returns:
            str --  file contents
        """
        with open(self.input_file, "r") as f:
            value = f.read()

        return value

    def write(self, text: str, display_text: str = "Output text: ") -> None:
        """Stdout or read from the file.

        Arguments:
            text {str} -- the text to use

        Keyword Arguments:
            display_text {str} -- Text to display before the provided text
            (default: {"Output text: "})

        """
        if self.output_file is None:
            return self.echo(display_text + text)
        return self.write_file(text)

    def echo(self, text: str) -> None:
        """Stdout the given text

        Arguments:
            text {str} -- the text to display
        """
        click.echo(text)

    def write_file(self, text: str) -> None:
        """Write to the file.

        Arguments:
            text {str} -- the output text.
        """
        with open(self.output_file, "w") as f:
            f.write(text)
