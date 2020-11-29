import json
from crayons import *

i = input('Enter the object ID Please : ')

id=int(i)

print(str(id))

with open('json.json','r') as file:
    payload=file.read()
    print(type(payload))
    json_payload=json.loads(payload)
    print(green(json_payload[id]['title'],bold=True))
    
    