import requests
import json
from crayons import blue, green, white, red, yellow,magenta, cyan

url = 'https://jsonplaceholder.typicode.com/photos'

response = requests.get(url)
#print(yellow(response.json(),bold=True))

print(yellow(json.dumps(response.json(),sort_keys=True,indent=4, separators=(',', ': ')),bold=True))