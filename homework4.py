

from flask import Flask, url_for, render_template, request
from pymongo import MongoClient

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')
    #return "This is the index page."

#@app.route("/login")
#def login():

@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('login.html', error=error)
 #   return "login webage"

@app.route("/user/<username>")
def profile(username):
    return 'This is %s ' % username

@app.route('/createwish', methods = ['POST'])
def createwish():
    firstName = request.form['firstName']
    lastName = request.form['lastName']
    zipcode = request.form['zipcode']
    return render_template('complete.html', firstName = firstName, lastName = lastName, zipcode = zipcode)

@app.route('/wish', methods = ['POST'])
def wish():
    #data = request.get_json(force=True)
    client = MongoClient('mongodb://daniel:daniel@linus.mongohq.com:10024/MSAN_697')
    db = client['MSAN_697']
    #print data
    test = db.test
    #test.insert(data)
    #print data
    wish = {}
    wish['firstname'] =  request.form['firstname']
    wish['lastname'] =  request.form['lastname']
    wish['zipcode'] = request.form['zipcode']
    wish['city'] = request.form['city']
    wish['address'] = request.form['address']
    wish['wish'] = request.form['wish']
    wish['age'] = request.form['age']

    test.insert(wish)

    return "wish insert"
    #
with app.test_request_context():
    print url_for('index')
    print url_for('login')
    print url_for('login',next='/')



if __name__ == '__main__':
    app.debug = True
    app.run()