from flask import Flask, jsonify, request, render_template, redirect, url_for
import random

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)


users = {"siwarha":"123", "clil":"fa12", "yahli":"123456", "tamar":"milki"}
facebook_friends=["Loai","Kenda","Avigail", "George", "Fouad", "Gi", "Daniela"]


@app.route('/', methods=['GET', 'POST'])  # '/' for the default page
def login():
	if request.method == 'GET':
  		return render_template('login.html')
	else:
		username2 = request.form['username'].lower()
		password2 = request.form['password']
		if username2 in users and password2==users[username2]:
			#return render_template('home.html')
			return redirect(url_for('home'))
		else:
			return render_template('login.html')

		return render_template('respond.html', username1 = username, password1 = password)

@app.route('/home')
def home():
	return render_template('home.html', facebook_friends = facebook_friends)

@app.route('/friend_exists/<string:name>')
def checkingFriend(name):
	return render_template('friend_exists.html', n = name, facebook_friends = facebook_friends)


  	


  



if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
    debug=True
	)
