from .models import Book
from django.forms import ModelForm
from django import forms

class BookForm(ModelForm):
	class Meta:
		model = Book
		fields = ['name', 'description', 'price','seller_name','contact_number','book_template']