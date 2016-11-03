
from flask import Flask, render_template, redirect, request, session, flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = "ThisIsSecret!"
def hasNumbers(string):
	return any(char.isdigit() for char in string)
@app.route('/', methods=['GET'])
def index():
  return render_template("index.html")
@app.route('/process', methods=['POST'])
def submit():
	Valid = True
	session['first_name'] = request.form['first_name']
	session['last_name'] = request.form['last_name']
	session['email'] = request.form['email']
	session['password'] = request.form['password']
	session['pass_conf'] = request.form['confirm']
	if len(request.form['first_name']) < 1:
		valid = False
		flash("Field Required", 'nameError')
	if hasNumbers(request.form["first_name"]) == True:
		valid = False
		flash("Must be letters", "nameError")
	if len(request.form['last_name']) < 1:
		valid = False
		flash("Field required", 'LnameError')
	if hasNumbers(request.form["last_name"]) == True:
		valid = False
		flash("Must be letters", 'LnameError')
	if len(request.form["email"]) < 1:
		flash("Email cannot be blank!", 'emailError')
	if not EMAIL_REGEX.match(request.form["email"]):
		valid = False
		flash("Invalid Email Address!", 'emailError')
	if len(request.form["password"]) < 8:
		valid = False
		flash("Password must be at least 8 characters long", 'passError')
	if session['password'] != session['pass_conf']:
		valid = False
		flash("Passwords must match", 'passError')
	if Valid:
		return redirect('/form')
	else:
		return redirect('/')
@app.route('/form')
def done():
	return render_template('Completed.html')
	
app.run(debug=True)