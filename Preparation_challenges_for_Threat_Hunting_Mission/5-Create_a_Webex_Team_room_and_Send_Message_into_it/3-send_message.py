import requests

URL = 'https://api.ciscospark.com/v1/messages'
ACCESS_TOKEN = '<your_access_token>'
ROOM_ID = '<room_id>'
MESSAGE_TEXT = '<message_text>'

MESSAGE_TEXT = 'Hello ! ( test )'

headers = {'Authorization': 'Bearer ' + ACCESS_TOKEN,
           'Content-type': 'application/json;charset=utf-8'}
post_data = {'roomId': ROOM_ID,
             'text': MESSAGE_TEXT}
response = requests.post(URL, json=post_data, headers=headers)
if response.status_code == 200:
    # Great your message was posted!
    #message_id = response.json['id']
    #message_text = response.json['text']
    print("New message created")
    #print(message_text)
    print("====================")
    print(response)
else:
    # Oops something went wrong...  Better do something about it.
    print(response.status_code, response.text)