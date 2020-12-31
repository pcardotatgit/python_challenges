#!/usr/bin/env python
"""
Copyright (c) 2018-2020 Cisco and/or its affiliates.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import requests
import time
from datetime import datetime
import json
import sys
from pathlib import Path
import requests
from crayons import blue, green, yellow, white, red,cyan
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import environment as env

# Disable insecure request warnings
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
    
# Functions
def get_amp_computers(
    host=env.AMP.get("host"),
    client_id=env.AMP_CLIENT_ID,
    api_key=env.AMP_API_KEY
):
    """Get a list of computers from Cisco AMP."""
    print("\n==> Computers from AMP")
    # Construct the URL
    url = f"https://{client_id}:{api_key}@{host}/v1/computers"
    response = requests.get(url, verify=False)
    response.raise_for_status()
    computers_list = response.json()["data"]   
    return computers_list

# If this script is the "main" script, run...
if __name__ == "__main__": 
    computers=get_amp_computers()  
    print(cyan(computers))
    print(green("======================="))
      
 
