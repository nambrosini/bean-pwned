#!/usr/bin/python3

import hashlib
import sys
import requests
import getpass

URL = "https://api.pwnedpasswords.com/range/"

password = getpass.getpass()

hash = hashlib.sha1(password.encode('utf-8')).hexdigest()

response = requests.get(URL + hash[:5], allow_redirects=False).text
lines = response.split('\n')

result = ''

for l in lines:
    if hash[5:].upper() in l:
        result = l
        break

if not result:
    print("The password provided was not found")
    sys.exit(0)

print("The password provided was found!")
print("Hash {}, occurences {}".format(hash, result.split(':')[1]))
