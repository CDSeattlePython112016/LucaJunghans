from django.shortcuts import render, redirect
import string
import random

# Create your views here.
def id_generator(size=14, chars=string.ascii_uppercase + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))

def index(request):
	if 'count'  not in request.session:
		request.session['count'] = 0
		return redirect ('/')

	return render(request, 'generator/index.html')

def generate(request):
	if request.method == "POST":
		request.session['count'] += 1
		request.session['word'] = id_generator(size=14, chars=string.ascii_uppercase + string.digits)
		return redirect('/')
	else:
		return redirect('/')

def refresh(request):
	if request.method == "POST":
		request.session.flush()
		return redirect ('/')
	else:
		return redirect('/')
