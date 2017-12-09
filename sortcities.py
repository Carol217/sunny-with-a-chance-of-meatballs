# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 12:07:45 2017

@author: hsshp15
"""
import json

countrylist= {}

data = json.load(open('city.list.json'))

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
    