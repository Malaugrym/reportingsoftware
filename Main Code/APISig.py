# test of signature generation

import hashlib
import random
import base64
import urllib
import hmac
import json
import urllib.request  as urllib2

apikey = "6f435992-ff82-408e-8ea2-b908c6bf6d0b"
secretkey = b'MjdmNzA0YzQtNGNiMi00M2UyLWJhMmYtYTc1YWI1OWQwN2I3NDc5OWYwMTItOGU3ZC00Y2YzLWJjNzItNzQ3ZjBlMjU0MmQz'


# Generates a random string of ten digits

salt = str(random.getrandbits(32))
salt2 = salt.encode('utf-8')

print (salt)

 # Computes the signature by hashing the salt with the secret key as the key

signature = hmac.new(secretkey, msg=salt2, digestmod=hashlib.sha256).digest()

 # base64 encode...#

encodedSignature = base64.encodestring(signature)
# ## # urlencode...
encodedSignature = urllib2.quote(encodedSignature)
#
print ("Voila! A signature: " + encodedSignature)


url = 'https://summithosting.kayako.com/api/v1/search/?query=brian'


url = url + '&apikey=' + apikey

url = url + '&salt=' + salt

url = url + '&signature=' + encodedSignature

print (url)
#
print (json.load(urllib2.urlopen(url)))
