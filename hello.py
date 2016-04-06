# coding=utf-8
import os
from flask import Flask, render_template,session,redirect,url_for,flash
from flask import make_response
from flask.ext.script import Manager
from flask.ext.bootstrap import Bootstrap
from flask.ext.moment import Moment

app = Flask(__name__)
app.config['SECRET_KEY'] = 'K60855D593F732ec push K21459a4868B9A7E'
manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)

from flask.ext.wtf import Form
from wtforms import StringField,SubmitField
from wtforms.validators import Required
class NameForm(Form):
	name = StringField('What is you name?',validators=[Required()])
	submit = SubmitField('Submit')


#配置数据库ORM
from flask.ext.sqlalchemy import SQLAlchemy
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
db = SQLAlchemy(app)

class Role(db.Model):
	__tablename__ = 'roles'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(64), unique=True)
	users = db.relationship('User',backref='role')

	def __repr__(self):
		return '<Role %r>'%self.name
class User(db.Model):
	__tablename__ = 'users'
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(64), unique=True,index=True)
	role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))

	def __repr__(self):
		return '<User %r>' % self.username

@app.route('/',methods=['GET','POST'])
def index():
	form = NameForm()
	if form.validate_on_submit():
		user = User.query.filter_by(username=form.name.data).first()
		if user is None:
			user = User(username = form.name.data)
			db.session.add(user)
			session['known'] = False
		else:
			session['known'] = True
		session['name'] = form.name.data
		form.name.data = ''
		return redirect(url_for('index'))
	return render_template('index.html', form=form, name=session.get('name'),known=session.get('known',False))


@app.route('/res')
def res():
	response = make_response('<h1>Response idle</h1>')
	response.set_cookie('answer', '42')
	return response


@app.route('/redirect')
def req():  # 函数名字不能和redirect() 有冲突
	# url_for('username', name='redirect')
	return render_template("user.html", name='Redirect')


@app.route('/user/<name>')
def username(name):
	classmates = ['Michael', 'Bob', 'Tracy']
	return render_template('user.html', name=name, comments=classmates)


@app.route('/bsbase')
def bsbase():
	return render_template("bs_bash.html")





if __name__ == '__main__':
	# manager.run()
	app.run(debug=True, port=35173)
