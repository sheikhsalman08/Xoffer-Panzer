from mongoengine import Document, fields
from mongoengine import *
from PanZer.settings import DBNAME

connect(DBNAME)

class Post(Document):
	title = StringField(max_length=120,required=True)

	def __str__(self):
		return self.title
