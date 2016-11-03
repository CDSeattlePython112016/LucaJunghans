from flask import Flask, render_template, request, redirect, session, flash
import os
app = Flask(__name__)
app.secret_key = 'thisIsSecret'#security
#routing rules below
@app.route('/')
def index():
  return render_template("index.html")
@app.route('/users', methods=['POST'])
def create_user():
   # notice how the key we are using to access the info corresponds with the names
   # of the inputs from our html form
   session['name'] = request.form['name']
   session['email'] = request.form['email']
   session['favorite'] = request.form['favorite']
   return redirect('/process')
@app.route('/process')
def process():
	if len(session['name']) < 1 and len(session['email']) < 1 and len(session['favorite']) < 1:
		flash("Name can't be empty", 'nameError')
		flash("Email can't be empty", 'emailError')
		flash("Favorite Ice Cream Can't be empty", 'favError')
		return redirect('/')
	if len(session['name']) < 1:
		flash("Name can't be empty", 'nameError')
		return redirect('/')
	if len(session['email']) < 1:
		flash("email cant be empty", 'emailError')
		return redirect('/')
	if len(session['favorite']) < 1:
		flash("Need Favorite", 'favError')
		return redirect('/')
	if len(session['name']) > 120:
		flash("name too long, 'nameError")
		return redirect('/')
	if len(session["email"]) > 120:
		flash("email too long", 'emailError')
		return redirect('/')
	if len(session["favorite"]):
		flash("Ice Cream too long", 'favError')
	else:
		pass
	return redirect('/show')


	
 


@app.route('/show')
def show_user():
  return render_template('survey.html')
app.run(debug=True)