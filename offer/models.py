from django.db import models
from mongoengine import Document,fields
from mongoengine import *
from PanZer.settings import DBNAME

connect(DBNAME)

# class Post(Document):
#     title = StringField(max_length=120, required=True)
#     content = StringField(max_length=500, required=True)
#     last_update = DateTimeField(required=True)
    
class Offer(Document):
	# id = fields.StringField(primary_key=True, default=ObjectId)
	name = fields.StringField(null=True)
	brand_name = fields.StringField(null=True)
	address = fields.ListField()
	details = fields.StringField(null=True)

	# created_date = fields.DateTimeField()
	created_date = fields.StringField(null=True)
	last_update_date = fields.StringField(null=True)
	# starting = fields.ListField()
	starting = fields.DictField()
	ending = fields.DictField()

	img_url = fields.ListField()
	keywords = fields.ListField()
	shopping_mall = fields.ListField()
	category = fields.ListField()
	sub_category = fields.ListField()

	def __str__(self):
		return self.name
