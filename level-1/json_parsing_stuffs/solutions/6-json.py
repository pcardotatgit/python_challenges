import json
import requests

with open('json_data-1.json') as json_data:
	json_data_2=json.load(json_data)
	list_keys = [ k for k in json_data_2 ]
	for x in list_keys:
		print(x['title'])
		if x.get('address'):
			print(x['address'][0]['ip'])
		else:
			print('No IP ADDRESS')