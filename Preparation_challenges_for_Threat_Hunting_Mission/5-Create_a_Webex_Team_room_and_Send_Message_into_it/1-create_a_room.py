import requests

URL = 'https://webexapis.com/v1/rooms'
ACCESS_TOKEN = '<your_access_token>'


headers = {'Authorization': 'Bearer ' + ACCESS_TOKEN,
           'Content-type': 'application/json;charset=utf-8'}
post_data = {'title': ROOM_NAME}
response = requests.post(URL, json=post_data, headers=headers)
if response.status_code == 200:
    print("New Room created")
    print("====================")
   print(json.dumps(response.json(),sort_keys=True,indent=4, separators=(',', ': ')))
else:
    # Oops something went wrong...  Better do something about it.
    print(response.status_code, response.text)