# solution from aymen gasmi
#import
import requests
import json
import sqlite3

# get the jason objects from the given url
target_url = "https://jsonplaceholder.typicode.com/photos"
response = requests.get (target_url)
urllist = response.json
# create a data base and a table Liste
conn = sqlite3.connect('THE_BASE.db')
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS Liste(
     id INTEGER PRIMARY KEY,
     title varchar(256),
     url varchar(256),
     thumbnailUrl varchar(256)

)
""")
conn.commit()
# insert element in the table
for i in urllist():
    if i['title'].endswith("corporis"):
        cursor.execute("""
        INSERT INTO Liste(id, title, url,thumbnailUrl) VALUES(:id, :title, :url,:thumbnailUrl)""", i)

        #print (i['title'])

#print the table
cursor.execute("""SELECT url from Liste where id in(2878, 3685,4633) """)
ay = cursor.fetchall()
print(ay)
f = open('test.html','w')

message = """<html>
<style>
table, th, td {
    border: 1px solid black;
}
</style>
<head></head>
<body>
  <table style="width:70%">
  <h2>Table</h2>
  <tr>
    <th><a href="https://via.placeholder.com/600/b9d504"> image1 </a></th>
    <th><a href="https://via.placeholder.com/600/1835a8"> image2 </a></th> 
    <th><a href="https://via.placeholder.com/600/7324d1"> image3 </a></th>
  </tr>
</table></body>
</html>"""

f.write(message)
f.close()
