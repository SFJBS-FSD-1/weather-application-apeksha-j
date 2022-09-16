from flask import Flask,render_template, request
import requests
# import urllib.request as myrequest
import json
import datetime

app = Flask(__name__) #creating instance of flask

@app.route("/",methods=["GET","POST"]) #@ is a decorator
def myweather():
    if request.method=="POST":
        city=request.form["city"]
        print(city)
        api= "ddb88d554a1c4fc343fe9c1d4c6b601d"
        url="http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+api+"&units=metric"
        print(url)
        # source=myrequest.urlopen(url).read() #removed
        response = requests.get(url).json()
        print(response)
        if response["cod"]==200:
            #data = json.loads(response)
            data={"temp":response["main"]["temp"],"place":response["name"],"lon":response["coord"]["lon"],"lat":response["coord"]["lat"],"sunrise":datetime.datetime.fromtimestamp(response.get('sys')['sunrise']),"sunset":datetime.datetime.fromtimestamp(response.get('sys')['sunset']),"status":200}
            # print(data["temp"])
            return render_template("home.html",data=data)
        elif response["cod"]== "404":
            data = {"message":response["message"],"status":404}
            return render_template("home.html",data=data)
    else:
        data= None
        return render_template("home.html",data=data)

app.run()
#