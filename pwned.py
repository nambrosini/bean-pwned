#!/usr/bin/python3

import hashlib
import sys
import requests

URL = "https://api.pwnedpasswords.com/range/"

if len(sys.argv) == 0:
    print("Not enough arguments provided.")
    sys.exit(1)

password = sys.argv[1].encode('utf-8')

sha_1 = hashlib.sha1()
sha_1.update(password)

hash = sha_1.hexdigest()

response = requests.get(URL + hash[:5]).text
lines = response.split('\n')

result = ''

for l in lines:
    if hash[5:].upper() in l:
        result = l
        break

if not result:
    print("{} was not found".format(sys.argv[1]))
    sys.exit(0)

print("{} was found!".format(sys.argv[1]))
print("Hash {}, occurences {}".format(hash, result.split(':')[1]))