from django.shortcuts import render, redirect, HttpResponse, reverse
from django.contrib import messages
from models import Book
# Create your views here.

def new_book(request):
	book = Book.objects.create_book(request.POST)
	context = {
		"books": Book.objects.all(),
		"user": request.session['user']
	}

	if book['created']:
		messages.success(request, "Added review for {}".format(book['new_book'].book_title))
	else:
		for error in book["errors"]:
			messages.error(request, error)
	
	return render(request,'books/new_book.html', context)

def books(request):
    if not 'user' in request.session:
        return redirect(reverse('index'))
    context = {
		"books": Book.objects.all(),
		"users": request.session['user']
		
	}


    return render(request, 'books/index.html', context)


def abook(request, book_id):
	context = {
		'book_id': Book.objects.all().filter(id = book_id)
	}
	return render(request, 'books/book_id.html', context)




def display(request):

	context = {
		"books": Book.objects.all(),
		
	}

	return render(request,'books/new_book.html', context)


def print_messages(request, message_list):
    for message in message_list:
        messages.add_message(request, messages.INFO, message)   
