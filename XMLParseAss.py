# Extracting Data from XML

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl
import Beautifulsoup

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/comments_75688.xml'
# url = 'http://py4e-data.dr-chuck.net/comments_42.xml'
# url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()  # Reading data from web and converting into readable form (html)
# print(html)
print(type(html))
tree =  ET.fromstring(html)
print(tree)
lst = tree.findall('comments/comment')
print(lst)
print('Total number of count element in XML is: ', len(lst))
sum = 0
for item in lst:
    print('Count: ', item.find('count').text)
    sum = sum + int(item.find('count').text)

print('Sum: ', sum)