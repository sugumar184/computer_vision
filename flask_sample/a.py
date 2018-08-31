from flask import Flask,render_template,request,g,url_for,redirect,session
from flask_pymongo import PyMongo
import os,json
app = Flask(__name__)
app.secret_key='asdf'

mongo_username = 'mv_user'
mongo_pass = '391#jI*(q'

app.config['MONGO_DBNAME'] = 'mv_nlp'
app.config['MONGO_URI'] = 'mongodb://%s:%s@192.168.1.242:27017/mv_nlp'%(mongo_username, mongo_pass)

mongo = PyMongo(app)
user = mongo.db.collection
@app.route('/')
def index():
    return redirect('home')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        session.pop('user', None)
        t_user = request.form['username']
        t_pass = request.form['password']
        user_data = user.find_one({"username": t_user})
        if user_data:
            if t_pass == user_data['password']:
                session['user'] = t_user
                return redirect(url_for('main_page', u_name=t_user))
            else:
                return 'wrong user or password'
        else:
            return redirect(url_for('signup'))
    return render_template('login.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        session.pop('user', None)
        user_data = user.find_one({"username": request.form['username']})
        if user_data:
            return 'User already exists'
        else:
            t_user = request.form['username']
            t_pass = request.form['password']
            if t_user is not None and t_pass is not None:
                user.insert({'username': t_user, 'password': t_pass})
            return redirect('login')
    return render_template('signup.html')

@app.before_request
def before_request():
    g.user = None
    if 'user' in session:
        g.user = session['user']


@app.route('/main_page', methods=['GET','POST'])
def main_page():
	if request.method == 'POST':
		session.pop('user', None)
		return redirect('/home')
	else:
	    u_name=request.args['u_name']
	    if g.user:
	        return render_template('main_page.html', u_name=u_name)
	    return redirect('home')    


if __name__ == '__main__':
    app.run(debug=True)

