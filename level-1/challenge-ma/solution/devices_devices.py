import json

payload={
	"devices": [{
		"Device": "Cisco ASA",
		"Type": "Firewall",
		"OS": "Cisco ASA OS",
		"Interfaces": [{
				"IF": "Interface 1",
				"Status": "UP",
				"Name": "inside",
				"ip_address": "192.168.1.254",
				"Mask": "/24"
			},
			{
				"IF": "Interface 2",
				"Status": "UP",
				"Name": "outside",
				"ip_address": "92.34.25.26",
				"Mask": "/24"
			}
		],
		"Status": "Clean"
	},
	{
		"Device": "User_Mktg-1",
		"Type": "workstation",
		"OS": "Windows 10",
		"Interfaces": [{
				"IF": "Interface 1",
				"Status": "UP",
				"Name": "Wireless lan",
				"ip_address": "192.168.1.12",
				"Mask": "/24"
			}
		],
		"Status": "Infected"
	}	
	]
}

print(json.dumps(payload,sort_keys=True,indent=4, separators=(',', ': ')))