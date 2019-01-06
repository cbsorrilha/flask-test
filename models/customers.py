from mongoengine import Document, StringField, DateTimeField, IntField
import datetime

class Customers(Document):
  name = StringField()
  address = StringField()
  telephone = StringField()
  email = StringField()
  origin = StringField()
  status = StringField()
  createdAt = DateTimeField(default=datetime.datetime.utcnow)
  updatedAt = DateTimeField(default=datetime.datetime.utcnow)
  v = IntField(db_field='__v')
  meta = {
    'indexes': [
      { 
        'fields': [
          "$name",
          "$address",
          "$telephone",
          "$email",
        ]
      }
    ]
  }