from flask import Flask, render_template, request, redirect, Response, url_for, session, flash
import os
from functools import wraps

app = Flask(__name__)

app.secret_key = 'secret key'

def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('login'))
    return wrap

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')

@app.route('/all')
@login_required
def all():
    docu = os.listdir('C:/Users/Drescu/Desktop/app/templates/') #method used to get the list of all files in directory specified
    this_list = []
    for d in docu:
        this_list.append(d.rsplit('.',1)[0]) # uses method .rsplit to strip the .html from end of strings, appends to list for all page
    return render_template('all.html', var_pages = this_list) #then a for loop is used with list var_pages to iterate over each item in list and print it as hypertext link

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid credentials. Please try again.'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('all'))
    return render_template('login.html', error=error)

@app.route('/logout')
@login_required
def logout():
    session.pop('logged_in', None) #will logout user by 'popping in true value with false'
    flash('You were logged out')
    return redirect (url_for('welcome'))

@app.route('/')
def blank():
    return redirect (url_for('welcome'))

@app.route('/edit/<path>', methods = ['GET','POST'])
@login_required
def edit(path):
    #if request.method == 'GET':
    pathway = 'C:/Users/Drescu/Desktop/app/templates/' + path + '.html'
    return Response(open(pathway).read(), mimetype= 'text/plain')

if __name__ == "__main__":
    app.run(debug=True)