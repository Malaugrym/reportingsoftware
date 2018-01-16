# test of signature generation

import hashlib
import random
import base64
import urllib
import hmac

apikey = "7b8cf4b7-ca83-4fdf-90af-095a193b0f88"
secretkey = "ZGQzZjRjNGYtZjhjNS00ZDdmLTk2MzctZGQzODgyMTZhYzg0OTFlZDI0YjgtZTc3My00YWI1LWE2MmYtNzhiNjhiZTc0MzM3"

# Generates a random string of ten digits
salt = str(random.getrandbits(32))
print (salt)

# Computes the signature by hashing the salt with the secret key as the key
signature = hmac.new(secretkey, msg=salt, digestmod=hashlib.sha256).digest()

# base64 encode...
encodedSignature = base64.encodestring(signature).replace('\n', '')

# urlencode...
encodedSignature = urllib.quote(encodedSignature)

print ("Voila! A signature: " + encodedSignature)
