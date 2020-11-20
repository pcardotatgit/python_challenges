#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Solution from Olivier Piquenot
import requests
import sqlite3
import sys
import http.server
import socketserver

def get_data(address):
    try:
        r=requests.get(address)
    except requests.exceptions.RequestException as e:
        print(e)
        sys.exit(1)
    if r.status_code != requests.codes.ok :
        print('Error received while GET:'+r.url)
        print(r.text)
        sys.exit('Error accessing URL:'+str(r.status_code))
    return(r)
    
def filter_data(data, chaine):
    exit_data=[]
    for i in data.json():
        if i['title'].endswith(chaine):
            exit_data.append(( i['id'], i['title'], i['url'], i['thumbnailUrl'] ))
    return(exit_data)

def data_to_db(data):
    sql_create="CREATE TABLE IF NOT EXISTS Liste ( id text PRIMARY KEY, title text, url text, thumbnailUrl text);"
    sql_add="INSERT OR REPLACE into Liste (id, title, url, thumbnailUrl) VALUES (?,?,?,?);"    
    with sqlite3.connect(':memory:') as conn:
        c=conn.cursor()
        try:
            c.execute(sql_create)
        except:
            sys.exit("couldn't create database")
        try:
            c.executemany(sql_add, data)
        except:
            sys.exit("Error adding data to db")
        return(c)
    return()

def present_data_web(cursor):
    port=9300
    Handler=http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("127.0.0.1", port), Handler) as httpd:
        print("serving at port", port)
        httpd.serve_forever()
    return()
    
def write_html(cursor, out_file):
    sql='select url from Liste where id = "2878" or id = "3685" or id = "4633";'
    try:
        cursor.execute(sql)
    except:
       sys.exit("error executing sql")
    results=[]
    for i in cursor.fetchall():
        results.append(i[0])
    with open ( out_file , 'w' ) as f:
        f.write('<!DOCTYPE html> <html> <body><tr>')
        for i in results:
            f.write('<td><img src="'+i+'"></td>')
        f.write("</tr></body> </html>")
    return()
        
def main():
    response=get_data('https://jsonplaceholder.typicode.com/photos')
    exit_data=filter_data(response, 'corporis')
    cursor=data_to_db(exit_data)
    if cursor :
        write_html(cursor, "page.html")
    present_data_web('')
    
if __name__=='__main__':
    main()