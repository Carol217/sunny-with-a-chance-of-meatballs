 # -*- coding: utf-8 -*-
"""
weather
u:cd 
p:b
"""

from flask import Flask, render_template, request
import json
import requests

#json of city codes
data_file = open('city.list.json')
data = json.load(data_file)

#get a json from an url
def getjson(url):
    result = requests.get(url).json()
    return result
    
key = "058432795340dade2316e429dcb44099"

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Check ur weather at ur <a href="/locations">location</a>'
    
    
@app.route('/locations')
def cities():
    return render_template("citylist.html", lst=data)
    
@app.route('/query')
def query():
    #create a link
    link = "http://api.openweathermap.org/data/2.5/weather?id=" \
    + request.args["id"] + "&appid=" + key
    jsn = requests.get(link).json()
    '''Test
    jsn = requests.get("http://samples.openweathermap.org/data/2.5/weather?id=2172797&appid=b1b15e88fa797225412429c1c50c122a1").json()
    '''    
    return render_template("weather.html", entry=jsn)

if __name__ == "__main__":
    app.debug = True
    app.run()
