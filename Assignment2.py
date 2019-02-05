# To run this, you can install BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4

# Or download the file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = 'http://py4e-data.dr-chuck.net/known_by_Fikret.html'
# url = input('Enter - ')
count = 4
position = 3
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')
# print(tags)
for i in range(count):
    link = tags[position].get('href',None)
    print(tags[position].contents[0])
    html = urllib.request.urlopen(link).read()
    soup = BeautifulSoup(html,'html.parser')
    tags = soup('a')