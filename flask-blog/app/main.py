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

'''@app.route('/edit/<page>', methods = ['GET','POST'])
def edit(page):
    if request.method == 'GET':
        return'''

@app.route('/all')
def all():
    direc = os.path.join(os.path.dirname(__file__)) + '/templates/'
    docu = os.listdir(direc)
    this_list = []
    for d in docu:
        this_list.append(d.rsplit('.html',1)[0])
    print (docu)
    return render_template('all.html', var_pages = this_list)


if __name__ == "__main__":
    app.run(debug=True)