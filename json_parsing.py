import json
import urllib.request, urllib.parse, urllib.error
import ssl

url = 'http://py4e-data.dr-chuck.net/comments_304842.json'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

uh = urllib.request.urlopen(url, context=ctx)
data = uh.read()

info = json.loads(data)
sum = 0
for element in info['comments']:
    sum += element['count']

print('Sum:', sum)