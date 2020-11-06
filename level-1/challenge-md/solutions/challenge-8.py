import json
from crayons import *
import requests
import sys

response=requests.get('https://jsonplaceholder.typicode.com/photos')
payload=response.content

line=''

json_payload=json.loads(payload)
for item in json_payload:
    id=item['id']
    title=item['title']
    url=item['url']
    thumbnailUrl=item['thumbnailUrl']
    line+=f"{id};{title};{url};{thumbnailUrl}\n"

with open('photo.csv','w') as output_file:
    output_file.write(line)
print(green("DONE",bold=True))
