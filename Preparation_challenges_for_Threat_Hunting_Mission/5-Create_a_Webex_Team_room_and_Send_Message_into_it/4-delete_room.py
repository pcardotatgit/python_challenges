import requests
import json

ACCESS_TOKEN = '<YOUR ACCESS TOKEN>'
ROOM_ID = '<ROOM_ID>'
URL = f'https://webexapis.com/v1/rooms/{ROOM_ID}'
print(URL)
headers = {'Authorization': 'Bearer ' + ACCESS_TOKEN,
           'Content-type': 'application/json;charset=utf-8'}

response = requests.delete(URL, headers=headers)
print(type(response))
if response.status_code == 204:
    print('ROOM DELETED')
    print('============================')
    print(json.dumps(response.json(),sort_keys=True,indent=4, separators=(',', ': ')))
else:
    # Oops something went wrong...  Better do something about it.
    print(response.status_code, response.text)
