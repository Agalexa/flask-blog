from flask import Flask, render_template, request, redirect, Response, url_for, session, flash
import os

app = Flask(__name__)

app.secret_key = 'secret key'

@app.route('/')
def blank():
    return render_template('index.html')

@app.route("/home")
def home():
    return render_template("home.html")
    
@app.route("/about")
def about():
    return render_template("about.html") 

@app.route('/random')
def random():
    return render_template('random.html')

@app.route('/<user>')
def user(name):
    return '<h1>Greatings, %s!</h1>' % user

@app.route('/edit/<path>', methods = ['GET','POST'])
def edit(path):
    #if request.method == 'GET':
    pathway = 'C:/Users/Drescu/Desktop/py-test/app/templates/' + path + '.html'
    return Response(open(pathway).read(), mimetype= 'text/plain')

@app.route('/all')
def all():
    #direc = 'C:/Users/Drescu/Desktop/py-test/app' + '/templates/'
    #direc = os.path.join(os.path.dirname(__file__)) + '/templates/'
    docu = os.listdir('C:/Users/Drescu/Desktop/py-test/app/templates/') #method used to get the list of all files in directory specified
    this_list = []
    for d in docu:
        this_list.append(d.rsplit('.',1)[0]) # uses method .rsplit to strip the .html from end of strings, appends to list for all page
        #this_list.append(d.rsplit('.html',1)[0]) #uses .append method 
    #print (" this is direc: " + direc)
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
def logout():
    session.pop('logged_in', None) #will logout user by 'popping in true value with false'
    flash('You were logged out')
    return redirect (url_for('all'))

if __name__ == "__main__":
    app.run(debug=True)