
from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["SECRET_KEY"] = "blah"
app.config["MONGO_URI"] = "blah"

# Create a new client and connect to the server
mongodb_client = PyMongo(app)
db = mongodb_client.db

from application import routes