from flask import Flask, render_template, jsonify, redirect
from flask_pymongo import PyMongo
import os
import scrape_mars
app = Flask(__name__)


#check if a MONGO_URL environment variable is set. If not, then use development environment and set it to the localhost
MONGO_URL = os.environ.get('MONGO_URL')
if not MONGO_URL:
    MONGO_URL = "mongodb://localhost:27017/";
app.config['MONGO_URI'] = MONGO_URL

print('MONGO_URL: ', MONGO_URL)

try:
    mongo = PyMongo(app)
except:
    print("cannot start mongo")


@app.route("/")
def index():
    print("getting mars data from mongodb")
    mars = mongo.db.mars.find_one()
    return render_template("index.html", mars=mars)


@app.route("/scrape")
def scrape():
    mars = mongo.db.mars
    mars_data = scrape_mars.scrape()
    mars.update(
        {},
        mars_data,
        upsert=True
    )
    return redirect("http://localhost:5000/", code=302)


if __name__ == "__main__":
    app.run(debug=True)
