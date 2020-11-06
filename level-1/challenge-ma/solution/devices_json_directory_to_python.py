#payload example to reproduce with directory
payload='''
- devices": [{
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
'''

# create a device list
device_list=[]
# create a device dictionary
device={}
# add items to the dictionary
device.update({"Device": "Cisco ASA"})
device.update({"Type": "Firewall"})
device.update({"OS": "Cisco ASA OS"})

# create a interface list
interfaces_list=[]
# create an interface directory
interface={}
interface.update({"IF": "Interface 1"})
interface.update({"Status": "UP"})
interface.update({"Name": "inside"})
interface.update({"ip_address": "192.168.1.12"})
interface.update({"Mask": "/24"})  

# add the first interface to the interface list
interfaces_list.append(interface)
# clear the interface dictionary
interface.clear()
interface.update({"IF": "Interface 2"})
interface.update({"Status": "UP"})
interface.update({"Name": "outside"})
interface.update({"ip_address": "92.34.25.26"})
interface.update({"Mask": "/24"})

interfaces_list.append(interface)
interface.clear()
interface.update({"IF": "Interface 3"})
interface.update({"Status": "DOWN"})
interfaces_list.append(interface)
# clear the last interface directory
interface.clear()
# add the interface list the the device directory
device.update({"Interfaces":interfaces_list})
# add the last item to the device directory
device.update({"Status":"Clean"})
# Append the first device to the device list
device_list.append(device)
#clear the interface list
interfaces_list.clear()

# clear the last device directory
device.clear()
device.update({"Device": "User_Mktg-1"})
device.update({"Type": "workstation"})
device.update({"OS": "Windows 10"})
interface.update({"IF": "Interface 1"})
interface.update({"Status": "UP"})
interface.update({"Name": "Wireless lan"})
interface.update({"ip_address": "192.168.1.12"})
interface.update({"Mask": "/24"})  
device.update({"Interfaces":interfaces_list})
device.update({"Status":"Infected"})

# Append the second device to the device list
device_list.append(device)

print(device_list)