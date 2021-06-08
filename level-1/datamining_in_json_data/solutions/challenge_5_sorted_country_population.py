'''
    sorted country population
'''
import json
import requests
from crayons import red,green,yellow,cyan
import sys

url = 'http://restcountries.eu/rest/v2/all?fields=name;population;region;capital;flag;borders'
response = requests.get(url)
print(cyan('======= PRINT RAW REQUEST RESULT ========'))
print(cyan(response))
print(type(response))
print(red('======= PRINT CONVERSION RAW TO LIST ========'))
json_data_1=response.json()
print(red(json_data_1))
print(type(json_data_1))
json_data_2=json.dumps(response.json())
with open('z_result.json','w') as file:
    file.write(json_data_2)
print(cyan('======= for each into list ========'))

'''
    Parse the JSON result and keep only items we are interested in
'''

dict_item={}
for item in json_data_1:
    line_out=item['name']+' : '+str(item['population'])
    #print(cyan(line_out))
    if item['name'] not in dict_item.keys():
        dict_item[item['name']]=item['population']
        
'''
    sort dictionnary entries based on values ( reverse=True / False  = ASC DESC )
'''        
sorted_values = sorted(dict_item.values(),reverse=True) # Sort the values
sorted_dict = {}

for i in sorted_values:
    for k in dict_item.keys():
        if dict_item[k] == i:
            sorted_dict[k] = dict_item[k]
            break
'''
    create a resulting list
'''
resulting_list=[]          
for name, population in sorted_dict.items():
    dict_item={}
    line_out=name+' : '+str(population)
    print(cyan(line_out,bold=True))
    dict_item[name]=population
    resulting_list.append(dict_item)

'''
    Goto every item of the list and print the result
'''
for item in resulting_list:
    print(cyan(item,bold=True))    

print(cyan('====== DONE ======='))
