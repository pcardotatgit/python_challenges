# Challenge

Read the list wich is located here :

	https://jsonplaceholder.typicode.com/photos

Sort all results with "title" ends with  : corporis 

Create a SQLi Database named [ THE_BASE ] and a table named [ List ]

with following fields :

- id
- title varchar(256)
- url varchar(256)
- thumbnailUrl varchar(256)

Fill this table with all previously parsed entries ( results with "title" ends with  : corporis  )

Launch the Python Embeded Web Server and listen on port 8888

From the SQLite Table create a static html page which is a html Table which contains only 3 rows and 2 columns.

The selected displayed lines will be lines with IDs : 2878, 3685 and 4633.

In column[0] display the title and in column[1] display the image corresponding to the URL ( an hot link )

Allocated Time : 4 hours if you are beginners.   60 minutes for those of you who already know how to do that