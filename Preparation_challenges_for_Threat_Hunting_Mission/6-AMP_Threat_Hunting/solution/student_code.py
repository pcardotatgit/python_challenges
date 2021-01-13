#!/usr/bin/env python

import requests
import time
from datetime import datetime
import json
import sys
from pathlib import Path
import requests
from crayons import blue, green, yellow, white, red,cyan
from requests.packages.urllib3.exceptions import InsecureRequestWarning

here = Path(__file__).parent.absolute()
repository_root = (here / "." ).resolve()
sys.path.insert(0, str(repository_root))

data_out={}

import environment_api_keys as env

client_id=env.AMP_CLIENT_ID
api_key=env.AMP_API_KEY

debug=1

# Disable insecure request warnings
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
def get_hostname_from_sha(query_params="",
    host=env.AMP.get("host"),
    client_id=env.AMP_CLIENT_ID,
    api_key=env.AMP_API_KEY,
):
    """Get a list of recent events from Cisco AMP."""
    print("\n==> Getting events from AMP")
    i_got_it=0
    if i_got_it==0:
        print(cyan(env.get_line(),bold=True))
        print (yellow("Second : Call the correct AMP API with the correct syntax...The API call which gives you the list of all infected endpoints "))
        print()
        print (yellow("Hint :"))
        print (yellow("https://api-docs.amp.cisco.com/api_actions/details?api_action=GET+%2Fv1%2Fevents&api_host=api.eu.amp.cisco.com&api_resource=Event&api_version=v1"))
        print()
        print (yellow("Change the value of i_got_it to 1 in order to move forward"))
        sys.exit()    
    #url = f"https://{client_id}:{api_key}@{host}/v1/events"
    response = requests.get(url, params=query_params, verify=False)
    if debug:
        print(cyan(env.get_line(),bold=True))
        print(cyan(response.json()))      
    # Consider any status other than 2xx an error
    response.raise_for_status()
    events_list = response.json()
    if debug:    
        events_list = response.json()
        print(green((events_list)))
        for events in events_list:
            #hostname=event['computer']['hostname'] 
            print(red(events))
    '''
    hostname=response.json()['data'][0]['computer']['hostname']
    return hostname     
    '''
    events_list = response.json()['data']
    return events_list
    
    
def get_amp_events(query_params="",
    host=env.AMP.get("host"),
    client_id=env.AMP_CLIENT_ID,
    api_key=env.AMP_API_KEY,
):
    """Get a list of recent events from Cisco AMP."""
    print("\n==> Getting events from AMP")
    url = f"https://{client_id}:{api_key}@{host}/v1/events"
    response = requests.get(url, params=query_params, verify=False)
    if debug:#PATRICK
        print(cyan(env.get_line(),bold=True))
        print(cyan(response.json()))      
    # Consider any status other than 2xx an error
    response.raise_for_status()   
    events_list = response.json()["data"]
    return events_list  

def get_amp_computers(
    host=env.AMP.get("host"),
    client_id=env.AMP_CLIENT_ID,
    api_key=env.AMP_API_KEY
):
    """Get a list of computers from Cisco AMP."""
    print("\n==> Computers from AMP")
    url = f"https://{client_id}:{api_key}@{host}/v1/computers"
    response = requests.get(url, verify=False)
    response.raise_for_status()
    computers_list = response.json()["data"]   
    return computers_list

def get_amp_computers_connector_id(
    host,
    client_id,
    api_key,
    hostname
):
    """Get a list of computers from Cisco AMP."""
    print("\n==> Computers from AMP")
    # Construct the URL
    url = f"https://{client_id}:{api_key}@{host}/v1/computers"
    response = requests.get(url, verify=False)
    response.raise_for_status()
    computers_list = response.json()["data"]
    for computer in computers_list:
        if computer['hostname']==hostname:
            comp_guid=computer['connector_guid']
    return comp_guid
    
def write_events_to_file(filepath, ampevents):
    with open(computers_path, "w") as file:
        json.dump(ampevents, file, indent=2)

if __name__ == "__main__":
    # Get the list of computers from AMP
    print (yellow("TODO :"))
    i_got_it=0
    if i_got_it==0: 
        print(cyan(env.get_line(),bold=True))
        print (yellow("First : assign the correct value to the variable : sha "))
        print (yellow("Change the value of i_got_it to 1 in order to move forward"))
        sys.exit()
        
    sha="01468b1d3e089985a4ed255b6594d24863cfd94a647329c631e4f4e52759f8a9"
    amp_query_params = f"detection_sha256={sha}" 
        
    i_got_it=0
    if i_got_it==0:
        print(cyan(env.get_line(),bold=True))
        print (yellow("Third : Call the correct function with the correct query params "))
        print (yellow("Hint : ")) 
        print (yellow("https://www.base64decode.org/"))  
        print (yellow("Here under the solution :"))
        print (yellow("aG9zdG5hbWVfbGlzdD1nZXRfaG9zdG5hbWVfZnJvbV9zaGEocXVlcnlfcGFyYW1zPWFtcF9xdWVyeV9wYXJhbXMp"))        
        print (yellow("Change the value of i_got_it to 1 in order to move forward"))
        sys.exit()   
    hostname_list="MISSION CALL THE CORRECT FUNCTION"   
    result=''
    for item in hostname_list:
        if item['computer']['hostname'] not in result:
            result+=item['computer']['hostname']+'\n'
    computers_path = repository_root / "resulting.json"
    print()
    print(yellow("Infected endpoint hostname list :"))
    print(green(result,bold=True))
    print(green("======================="))
