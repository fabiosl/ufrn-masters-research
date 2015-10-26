#!/usr/bin/python
import MySQLdb
import mysql_config
import requests
import json

fb = MySQLdb.connect(
    host = mysql_config.mysql_host,
    user = mysql_config.mysql_user,
    passwd = mysql_config.mysql_passwd,
    db = mysql_config.mysql_schema
)
# you must create a Cursor object. It will let
#  you execute all the queries you need
fb_cursor = fb.cursor() 

fb_cursor.execute("SELECT * FROM mestrado.post_all_pages_portugal_globo_pt limit 100;")
num_fields = len(fb_cursor.description)
field_names = [i[0] for i in fb_cursor.description]

def build_json_for_post(post_row):
    object = {}
    i=0
    for column in field_names:
        result = ""
        if post_row[i]:
            result = str(post_row[i])

        object[column] = result
        i+=1
    return str(json.dumps(object))

def insert_post_on_es(json_string):
    url = 'http://52.26.62.124:9200/facebook/post'
    values = json_string

    payload = values
    r = requests.post(url, data=payload)
    print(r.text)


for post in fb_cursor.fetchall():
    json_string = build_json_for_post(post)
    insert_post_on_es(json_string)

