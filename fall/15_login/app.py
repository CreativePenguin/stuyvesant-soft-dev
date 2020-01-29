# Winston Peng & Albert Wan -- Team Dental Hygeine
# SoftDev1 pd9
# K15 -- Do I Know You? -- Using Cookies, Login Page
# 10-2-2019
from flask import Flask, render_template, request, redirect, session
from utl import login as login_file
app = Flask(__name__)
app.secret_key = 'dentalhygeine'

logins = login_file.getDict()  # keys = usernames, values = passwords
global error_message  # This variable keeps track of whether it's a username error or a password error
error_message = None

@app.route("/")
def root():
    """ Redirects to login if no existing account, and to welcome page if already logged in """
    # Adds a new user
    print(request.args)
    if 'username' in request.args:
        login_file.addUser(request.args['username'], request.args['password'])
    # checks if username & password are already recorded
    if 'username' in session and 'password' in session:
        session_user = session['username']
        session_pwd = session['password']
        # verifies username and password
        if session_user in logins.keys():
            # verifies password separately to avoid null pointer
            if session_pwd == logins[session_user]:
                return redirect('/welcome')
    return redirect('/login')

@app.route('/login')
def login():
    global error_message
    print(error_message)
    return render_template(
        "page.html",
        error=error_message  # Prints out whether it's a username error, or password error
    )

@app.route("/auth")
def route():
    """this is a temporary page that checks if login was correct"""
    username = request.args['username']
    password = request.args['password']
    global error_message
    print(request.cookies)
    # logins.keys() holds all recognizable usernames
    if username not in logins.keys():
        error_message = 'Username not found'
        print(error_message)
        return redirect('/login')
    # checks to see if the dictionary match for the username is the password
    if logins[username] != password:
        error_message = 'Incorrect Password'
        print(error_message)
        return redirect('/login')
    # sets error message to none, so that login page will stop saying they have an error
    error_message = None
    session['username'] = username
    session['password'] = password
    return redirect('/welcome')

@app.route('/welcome')
def welcome():
    """prints welcome message in welcome page"""
    #user = request.args['username']
    global error_message
    return render_template(
        'welcome.html'
    )

@app.route('/newuser')
def newuser():
    """This is where people can make a new account"""
    global error_message
    error_message = None  # redirects back to "/" without going through other error message checks
    return render_template(
        'newuser.html'
    )

if __name__ == "__main__":
    app.debug = True
    app.run()
