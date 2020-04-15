# Code Review task 1
### A small python script implementing encryption, decryption and hacking of the most widespread encryption algorithms (Vigenere, Caesar, Vername).


## Build the project
Run the **build.sh** script to build the project. It will create the virtual environment, activate it and install all the needed pip packages: <br/>
`./build.sh`

## Usage
`./encryptor.py --help` - to display the help message.

### Encode
Use this command to encode the text (read from stdio or a file) using the available ciphers and display the encrypted text or write it to a file.

**Usage: `encryptor.py encode [OPTIONS]`**

Options:<br />
  `-c, --cipher [caesar|vigenere|vernam]` -- Cipher type: Caesar, Vigenere or Vernam. *[required]*<br />
  `-k, --key TEXT`         --         The key: integer for Caesar, string for Vigenere and Vernam.  *[required]*<br />
  `--input-file FILENAME`       --    The input file to read the text from.<br />
  `--output-file FILENAME`     --     Output file to write the text to.<br />


### Decode 
Use this command to decode the text (read from stdio or a file) using the available ciphers and display the encrypted text or write it to a file.

**Usage: `encryptor.py decode [OPTIONS]`**

Options:<br />
  `-c, --cipher [caesar|vigenere|vernam]`Cipher type: Caesar, vigenere or Vernam *[required]* <br />
  `-k, --key TEXT`                  The key: integer for Caesar, string for Vigenere and Vernam.  *[required]* <br />
  `--input-file FILENAME`           The input file to read the text from. <br />
  `--output-file FILENAME`          Output file to write the text to. <br />

## Features
- Encryption and decryption using the following ciphers:
  - Caesar cipher
  - Vegenere cipher
  - Vernam cipher
- The characters allowed to use (e.g. that will be encrypted) are. The rest of the characters will be escaped and left unchanged: ``abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZабвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ1234567890!"#$%&'()*+,-./:;<=>?@[\\]^_ `{|}~``

## Run the tests
`pytest`



