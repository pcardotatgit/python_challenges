# coding: utf-8
import requests
import re
import json

r = requests.get("http://www.jamessawyer[.]co[.]uk/MASTER[.]txt")
selection = re.findall('.*\.info\s', r.text)
print("status code is "+str(r.status_code))
print(r)

i=0
data={"web":[]}
for s in selection:
    data.get("web").append(s.strip())
    i+=1

data"nombre_resultat"]=i
json_data = json.dumps(data, indent=4)
print(json_data)

file=open("web.json","w")
file.write(json_data)
print("web.json as been created")
file.close()
