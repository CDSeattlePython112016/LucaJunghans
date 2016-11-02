from flask import Flask, render_template, request, redirect, session, flash
import random
app = Flask(__name__)
app.secret_key = 'thisIsSecret'

def makerand():
	session['num'] = random.randrange(0,101)
	

@app.route('/')
def main():
	if 'num' in session:
		pass
	else:
		makerand()
	return render_template("index.html")



@app.route('/game', methods=['post'])
def game():
	user = request.form['gameinput']
	print(user)
	print(session['num'])
	session['decision'] = ' '
	if user.isdigit():
		userval = int(user)
		if userval == session['num']:
			flash('Chicken Dinner','win' )
			return redirect ('/')
		elif userval > session['num']:
			flash('Guess too high', 'mistake')
		else: 
			flash('Guess too low', 'mistake')
	else:
		session['decision'] = "Not a number!"
	return redirect('/')



@app.route('/reset', methods=['GET'])
def playAgain():
	makerand()
	session['decision'] = ' '
	return redirect('/')
app.run(debug = True)
