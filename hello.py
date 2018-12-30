from flask import Flask
from flask import jsonify
from pymongo import MongoClient
from models import Customers
from mongoengine import connect
from string import Template
import os

USER = os.getenv('DB_USERNAME')
PASS = os.getenv('DB_PASSWORD')
URL_TEMPLATE = Template('mongodb://$user:$password@ds137720.mlab.com:37720/petvip')
HOST = URL_TEMPLATE.substitute(user=USER, password=PASS)

app = Flask(__name__)

connect('petvip', host=HOST)

@app.route("/")
def hello():
    return Customers.objects.first().to_json()