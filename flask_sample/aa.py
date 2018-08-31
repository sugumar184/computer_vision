from flask import Flask,render_template,request,g,url_for,redirect,session
from flask_pymongo import PyMongo
import os
app = Flask(__name__)
app.secret_key='asdf'

mongo_username = 'mv_user'
mongo_pass = '391#jI*(q'

app.config['MONGO_DBNAME'] = 'mv_nlp'
app.config['MONGO_URI'] = 'mongodb://%s:%s@192.168.1.242:27017/mv_nlp'%(mongo_username, mongo_pass)


@app.route('/login',methods=['GET','POST'])
def login():
	msg = 'sdf'
	return redirect(url_for('main_page', msg=msg))
	#return render_template('login.html')


@app.route('/main_page')
def main_page():
    msg=request.args['msg']
    #return render_template('main_page.html')
    return render_template('main_page.html', u_name=msg)
    
if __name__ == '__main__':
    app.run(debug=True)

