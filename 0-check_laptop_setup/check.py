import sys
import requests
import json

ACCESS_TOKEN = 'COPY AND PASTE HERE YOUR WEBEX BEARER TOKEN'

ROOM_ID = 'Y2lzY29zcGFyazovL3VzL1JPT00vNGRmZGEzYTYtZTczMC0zMjFjLTk5MjUtYzAyZjdhNjVjZWQ1'
if sys.prefix!=sys.base_prefix:
    headers = {'Authorization': 'Bearer ' + ACCESS_TOKEN,'Content-type': 'application/json;charset=utf-8'}
    URL = 'https://api.ciscospark.com/v1/people/me'
    response = requests.get(URL, headers=headers)
    user_email=response.json()['emails']
    display_name=response.json()['displayName']
    MESSAGE_TEXT=f'SETUP READY : for {display_name} : {user_email}'
    URL = 'https://api.ciscospark.com/v1/messages'
    post_data = {'roomId': ROOM_ID,'text': MESSAGE_TEXT}
    response = requests.post(URL, json=post_data, headers=headers)
    if response.status_code == 200:
        print('Well Done You are ready for the Python Labs !!')
        print('====================')
        print(response)
    else:
        print(response.status_code, response.text)
else:
    print()
    print('Your python virtual environment is not installed')