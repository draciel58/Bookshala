from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Book(models.Model):
	name = models.CharField(max_length=20,blank=True)
	posted = models.DateTimeField(default=datetime.now(),blank=True,null=True)
	description = models.TextField(blank=True)
	price = models.IntegerField(blank=True,null=True)
	seller_name = models.CharField(max_length=20,blank=True,null=True)
	contact_number = models.IntegerField(blank=True,null=True)
	book_template = models.ImageField(upload_to='book/image',blank=True,null=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.name

	@property	
	def get_photo_url(self):	
		if self.book_template and hasattr(self.book_template,'url'):
			return self.book_template.url
		else:
			return "media/cloneapp/image/chacha.jpg"


class Wishlist(models.Model):
	numid = models.IntegerField(blank=True,null=True)	
	name = models.CharField(max_length=20,blank=True)
	posted = models.DateTimeField(default=datetime.now(),blank=True,null=True)
	price = models.IntegerField(blank=True,null=True)
	seller_name = models.CharField(max_length=20,blank=True,null=True)
	contact_number = models.IntegerField(blank=True,null=True)
	book_template = models.ImageField(upload_to='book/image',blank=True,null=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.name

	@property	
	def get_photo_url(self):	
		if self.book_template and hasattr(self.book_template,'url'):
			return self.book_template.url
		else:
			return "media/cloneapp/image/chacha.jpg"