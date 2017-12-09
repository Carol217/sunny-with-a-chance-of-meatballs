# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 12:07:45 2017

@author: hsshp15
"""
import json
import sqlite3

f="cities.db"
db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops
   
countrylist= []

data = json.load(open('city.list.json'))
'''
for element in data:
    name = element["country"]
    if not name in countrylist:
        countrylist.append(name)
        statement = "CREATE TABLE IF NOT EXISTS '%s' (cityid INTEGER PRIMARY KEY, cityname TEXT)" % name
        c.execute(statement)
        db.commit()
'''
'''
with open ('countries.json', 'w') as d:
    d.write(json.dumps(countrylist))

'''

for element in data:
    name = element["country"]
    c.execute("INSERT INTO '" + name + "' VALUES (?, ?)", (element["id"], element["name"]))
    db.commit()

'''
for element in data:
    name = element["country"]
    if not name in countrylist:
        countrylist[name]= str("countries/" + name + ".json")
        #countrylist[name]= []
        #countrylist[name].append(str("countries/" + name + ".json"))
        #countrylist[name].append(open(countrylist[name][0], 'w'))
    #d = countrylist[name][1]
    #d.write(json.dumps(element))
        
with open ("countrylist.json", "w") as d:
    d.write(json.dumps(countrylist))
'''

db.commit() #save changes
db.close()  #close database