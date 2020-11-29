import requests
import json

URL = 'https://webexapis.com/v1/rooms'
ACCESS_TOKEN = '<your_access_token>'
ROOM_NAME = '<ROOM_ID>'


headers = {'Authorization': 'Bearer ' + ACCESS_TOKEN,
           'Content-type': 'application/json;charset=utf-8'}

response = requests.get(URL, headers=headers)
print(type(response))
if response.status_code == 200:
    print(json.dumps(response.json(),sort_keys=True,indent=4, separators=(',', ': ')))
else:
    # Oops something went wrong...  Better do something about it.
    print(response.status_code, response.text)