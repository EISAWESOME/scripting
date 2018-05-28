#!/usr/bin/env python3
import hashlib
import sqlite3
import re

conn = sqlite3.connect('sha.sqlite')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS sha
             (mot text, hash text)''')

with open("./mots_francais", "r") as l:
    array = []
    for line in l:
      #print(line.replace("'", " "))
      query = "INSERT INTO sha VALUES ('"+ line.replace("'", " ").replace('\n', ' ').replace('\r', '') +"', '"+ hashlib.sha512(line.encode('utf-8')).hexdigest() +"')"
      c.execute(query)
      #print(hashlib.sha512(line.encode('utf-8')).hexdigest())
conn.commit()
c.execute("SELECT * FROM sha")
print(c.fetchall())
