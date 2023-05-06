#!/usr/bin/python3

from flask import Flask, render_template, request, redirect, url_for
import sqlite3

# Create a database connection
conn = sqlite3.connect('users.db')
cursor = conn.cursor()

app = Flask(__name__)

# Create a table to store user information
cursor.execute('''CREATE TABLE IF NOT EXISTS users
				(
				username TEXT NOT NULL,
				password TEXT NOT NULL,
				email TEXT NOT NULL,
				phone TEXT,
				hostel TEXT)''')
conn.commit()

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/signup', methods=['POST','GET'])
def signup():
	username = request.form['username']
	password = request.form['password']
	email = request.form['email']
	phone = request.form['phone']
	hostel = request.form['hostel']
	
	# Insert the user information into the database
	cursor.execute('''INSERT INTO users (username, password, email, phone, hostel)
					VALUES (?, ?, ?, ?, ?)''', (username, password, email, phone, hostel))
	conn.commit()
	
	# Redirect the user to the login page
	return redirect(url_for('profile'))

@app.route('/login', methods=['POST'])
def login():
	username = request.form['username']
	password = request.form['password']
	
	# Check if the user exists in the database
	cursor.execute('''SELECT * FROM users WHERE username = ? AND password = ?''', (username, password))
	user = cursor.fetchone()
	if user is not None:
		# Redirect the user to the profile page
		return redirect(url_for('profile'))
	else:
		return redirect(url_for('signup'))


if __name__ == '__main__':
    app.run(debug=True)