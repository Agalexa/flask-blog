from flask import Flask, render_template, request, Response
import os

app = Flask(__name__)

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
        this_list.append(d.rsplit('.',1)[0]) # uses method .rsplit to strip the .html from end of strings, appends to list. 
        #this_list.append(d.rsplit('.html',1)[0]) #uses .append method 
    #print (" this is direc: " + direc)
    return render_template('all.html', var_pages = this_list)


if __name__ == "__main__":
    app.run(debug=True)