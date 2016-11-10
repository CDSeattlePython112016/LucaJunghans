from django.shortcuts import render, HttpResponse, redirect


# Create your views here.

def index(request):

	return render(request, 'server_app/index.html')

def process(request):
	if request.method == "POST":
		request.session['name'] = request.POST['name']
		request.session['location'] = request.POST['location']
		request.session['favorite'] = request.POST['favorite']
	if 'count' not in request.session:
		request.session['count'] = 1
	else:
		request.session['count'] += 1
	return redirect('/display')



def display(request):

	return render(request, 'server_app/display.html')

def refresh(request):
	if request.method == "POST":
		request.session.flush()
		return redirect ('/')
	else:
		return redirect('/')
