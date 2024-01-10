
from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["SECRET_KEY"] = "e943460b5c5d15b27a0755a6aa7326747ca69258"
app.config["MONGO_URI"] = "mongodb+srv://aaronroche:8dKk6LiqaUW7SDgY@cluster0.dixnrws.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
mongodb_client = PyMongo(app)
db = mongodb_client.db

from application import routes