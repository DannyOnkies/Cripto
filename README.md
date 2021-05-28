# Crypto
Random mono-alphabetic encryption

With this method you can encrypt a single text or a text file. 
You use the prompt command line by passing the required values to it.
You can ask for help with the -h option 

Mode -ENCRYPT-
------------------
The script returns text consisting of only letters
encrypting it with a key that is provided on it
line before the text.

Example> py crypto.py -enc KEYWORD HELLO
Result> ZOTTP

To encrypt a text file use the following
commands:

py crypto.py -etxt KEYWORD FILE_TO_ENCRYPT.TXT

Mode -DECRYPT-
------------------
The script returns the previously encrypted text
with the -encrypt option. The key used must be provided
in the encryption operation.

Example> py crypto.py -dec KEYWORD ZOTTP
Result> HELLO

To decrypt a text file, knowing the KEYWORD,
use the following commands:

py crypto.py -dtxt KEYWORD FILE_TO_DECRYPT.TXT
