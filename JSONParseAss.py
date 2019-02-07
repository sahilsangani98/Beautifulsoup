# Counting sum of count element from JSON file
import json
import urllib.request, urllib.parse, urllib.error
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/comments_75689.json'
# url = 'http://py4e-data.dr-chuck.net/comments_42.json'
html = urllib.request.urlopen(url, context=ctx).read()

info = json.loads(html)     # Info is JSON formatted data
# print("User Count: ", len(info))
print(info)
sum = 0
for item in info['comments']:
    print(item['count'])
    sum = sum + int(item['count'])
print('Sum: ', sum)
