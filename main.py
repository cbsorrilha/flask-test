import os
from flask import Flask, request
from string import Template
from mongoengine import connect
from controllers import CustomerController as Customers

USER = os.getenv('DB_USERNAME')
PASS = os.getenv('DB_PASSWORD')
URL_TEMPLATE = Template('mongodb://$user:$password@ds137720.mlab.com:37720/petvip')
HOST = URL_TEMPLATE.substitute(user=USER, password=PASS)

app = Flask(__name__)

connect('petvip', host=HOST)

@app.route("/customers")
def list():
  return Customers.list(request).to_json()

@app.route("/customers/<customerId>")
def getOne(customerId):
  return Customers.getOne(request, customerId).to_json()

@app.route("/customers/search")
def search():
  return Customers.search(request).to_json()