# OneTimePad

<img src="https://github.com/SRingshandl/OneTimePad/blob/main/Example_Image.png" width="100%">

Encrypts text from a text file and outputs an encrypted text file and a corresponding key.  
See https://en.wikipedia.org/wiki/One-time_pad for further details on methodology.

To ensure a cryptographically correct encryption the Python 3 library Secrets was used  
(see https://docs.python.org/3/library/secrets.html).

Usage on command line (on Windows cmd with installed Python 3):  
Encrypt: python OTP_encode.py EncryptMe.txt  
Decrypt: python OTP_decode.py EncryptMe_String1.txt EncryptMe_String2.txt

