import json
import urllib
import urllib.request as urllib2
import requests

url = 'https://summithosting.kayako.com/api/v1/users'

username = 'bparks@summithosting.com'
pw = 'Welcome1!'

req = requests.get(url, auth=requests.auth.HTTPBasicAuth(username,pw))

print (json.loads(req.text))
