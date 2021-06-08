import json
import sys

with open('json_resultat.txt') as r:
	resp = r.read()
	
#status_code = 200
if (status_code == 200):
	json_resp = json.loads(resp)
	resp2=json.dumps(json_resp,sort_keys=True,indent=4, separators=(',', ': '))
	version=json_resp["api_version"]
	samples = json_resp["data"]["items"]
	fh = open("resultat.txt", "w")
	for sample in samples:					
    if sample['severity'] == 80:
        i1=str(sample['timestamp'])	
        severite_str=str(sample['severity'])
        print('Sample : ' + sample['sample_id'] + ' = ' + severite_str + ' = ' + i1)
        donnee='Sample : ' + sample['sample_id'] + ' = ' + severite_str + ' = ' + i1
        fh.write(donnee)
        fh.write('\r\n')
	fh.close()

