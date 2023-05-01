# coding: utf-8
import requests
import re
import json

url="https://raw[.]githubusercontent.com/tg12/pihole-phishtank-list/master/list/phish_domains.txt"

r = requests.get(url)
selection = re.findall('.*\.co\s', r.text)
print("status code is "+str(r.status_code))
print(r)

i=0
data={"domains":[]}
for s in selection:
    data.get("domains").append(s.strip())
    i+=1

data["nb_of_domains"]=i
json_data = json.dumps(data, indent=4)
print(json_data)

file=open("web.json","w")
file.write(json_data)
print("web.json as been created")
file.close()
