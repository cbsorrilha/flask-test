import mongoengine
import datetime

class Customers(mongoengine.Document):
  name = mongoengine.StringField()
  address = mongoengine.StringField()
  telephone = mongoengine.StringField()
  email = mongoengine.StringField()
  origin = mongoengine.StringField()
  status = mongoengine.StringField()
  createdAt = mongoengine.DateTimeField(default=datetime.datetime.utcnow)
  updatedAt = mongoengine.DateTimeField(default=datetime.datetime.utcnow)
  v = mongoengine.IntField(db_field='__v')