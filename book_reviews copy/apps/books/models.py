from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Book_Manager(models.Manager):
	def create_book(self, data):
		errors = []
		if not data['title']:
			errors.append('Fields must not be blank!')
		elif len(data['review']) < 25:
			errors.append('This website is great because of the great content, please contribute by writing a review of substance!')

		response = {}

		if not errors:
			new_book = self.create(book_title = data['title'], author = data['author'], rating = data['rating'], review=data['review'], published = data['published'])
			response['created'] = True
			response['new_book'] = new_book
		else:
			response['created'] = False
			response['errors'] = errors
		return response


		





class Book(models.Model):
	book_title = models.CharField(max_length = 55)
	author = models.CharField(max_length = 55)
	review = models.CharField(max_length=2000, default=False)
	rating = models.IntegerField() 
	published = models.CharField(max_length=55, default=False)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)

	objects = Book_Manager()


