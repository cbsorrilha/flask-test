import pytest
from customers import Customers
from mongoengine import connect

def testModel():
  connect('mongoenginetest', host='mongomock://localhost')
  
  assert null in Customers