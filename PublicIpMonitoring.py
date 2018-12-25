
import requests

print(requests.get('http://ip.42.pl/raw').text)
print(requests.get("http://ipecho.net/plain?").text)

