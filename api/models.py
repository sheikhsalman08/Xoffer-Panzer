from django.db import models
from mongoengine import Document,fields

# Create your models here.
class Offers(Document):
	id = fields.IntField(primary_key=True)
	name = fields.StringField()
	food = fields.StringField()