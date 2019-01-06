import os
from flask import Flask
from string import Template
from mongoengine import connect
from routes.customers import customerRoutes

USER = os.getenv('DB_USERNAME')
PASS = os.getenv('DB_PASSWORD')
URL_TEMPLATE = Template('mongodb://$user:$password@ds137720.mlab.com:37720/petvip')
HOST = URL_TEMPLATE.substitute(user=USER, password=PASS)

app = Flask(__name__)

connect('petvip', host=HOST)

customerRoutes(app)
