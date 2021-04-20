import json
from crayons import *
#import requests
import sys

response=requests.get('https://www.prevision-meteo.ch/services/json/lat=46.259lng=5.235')
payload=response.content
json_payload=json.loads(payload)
heures=json_payload['current_condition']['hour'].split(":")
hour=int(heures[0])
hour=hour-1
if hour<0:
hour=23
if hour<10:
hour_str="0"+str(hour)
else:
hour_str=str(hour)
heure=hour_str+':'+heures[1]
print(json_payload['current_condition']['date'])
print(heure)
print(json_payload['current_condition']['tmp'])
