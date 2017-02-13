#main.py
import os
import random
from hashlib import sha256
from hmac import HMAC

def encrypt_password(password, salt=None):
    """Hash password on the fly."""
    if salt is None:
        salt = str(random.randint(10000000,99999999)) # 64 bits.

    assert 8 == len(salt)
    assert isinstance(salt, str)


    assert isinstance(password, str)

    result = password.encode('utf-8')
    salt = salt.encode('utf-8')
    for i in range(10):
        result = HMAC(result, salt, sha256).digest()

    return salt + result


while 1:
    ob = input('your ob password: ')
    salt = input('your 8 length salt: ')
    if len(salt) != 8:
    	print('salt should by 8 length')
    	pass
    else:
    	encrypt = encrypt_password(ob, salt)

    	print(encrypt)