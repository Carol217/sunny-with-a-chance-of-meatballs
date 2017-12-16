 # -*- coding: utf-8 -*-
"""
weather
u:cd 
p:b
"""

from flask import Flask, render_template, request
import json
import requests
import sqlite3

#list of city codes
data_file = open('countries.json')
data = json.load(data_file)
data_file.close()
#print json.dumps(data)

f="cities.db"
db = sqlite3.connect(f, check_same_thread = False) #open
c = db.cursor()

#get a json from an url
def getjson(url):
    result = requests.get(url).json()
    return result
    
key = "058432795340dade2316e429dcb44099"

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("countrylist.html", lst=sorted(data))
    
    
@app.route('/cities')
def cities():
    country= request.args["country"]
    command = "SELECT * FROM " + country
    c.execute(command)
    temp = c.fetchall()
    return render_template("citylist.html", lst=temp, country=request.args["country"])
    
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
