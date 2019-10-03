# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

entered_url = input('Enter first URL: ')

def retrieving_names(url, position_target):
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    position = 0
    # Retrieve all of the anchor tags
    tags = soup('a')
    for tag in tags:
        # Look at the parts of a tag
        #print('URL:', tag.get('href', None))
        position += 1
        if position < position_target:
            continue
        elif position == position_target:
            new_url = tag.get('href', None)
    return new_url

step = 1
name = list()
position_target = int(input('Enter position: '))
count = int(input('Enter count: '))
while step <= count:
    entered_url = retrieving_names(entered_url, position_target)
    if step == count:
        name = re.findall('^http://py4e-data.dr-chuck.net/known_by_(.+).html', entered_url)
    step += 1

print('\nThe answer is:', name[0])