import requests

r = requests.get('https://twitter.com/explore')

print(r.text)