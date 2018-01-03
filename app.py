from flask import Flask, render_template, jsonify, redirect
#from flask_pymongo import PyMongo
from pymongo import MongoClient
import os
import scrape_mars
app = Flask(__name__)


#created a mongo database on mlab called mars. Use this for the Heroku app
client = MongoClient("mongodb://mars:marspw@ds137957.mlab.com:37957/mars")
db =  client.mars
mars = db.mars


@app.route("/")
def index():
    print("getting mars data from mongodb")
    planet = mars.find_one()
    return render_template("index.html", mars=planet)


@app.route("/scrape")
def scrape():
    mars = db.mars
    mars_data = scrape_mars.scrape()
    mars.update(
        {},
        mars_data,
        upsert=True
    )
    #######return redirect("http://localhost:5000/", code=302)
    return redirect("mars-mission.herokuapp.com", code=302)

if __name__ == "__main__":
    app.run(debug=True)
