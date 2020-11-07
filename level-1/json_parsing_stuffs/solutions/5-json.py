import json
import requests

url = 'https://jsonplaceholder.typicode.com/photos'
response = requests.get(url)
json_data_2=json.dumps(response.json())
json_data_3=json.loads(json_data_2)
#print(json_data_2)
list_keys = [ k for k in json_data_3 ]
for x in list_keys:
	print(x['title'])
	