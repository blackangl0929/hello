from datetime import datetime
from flask import render_template,session,redirect,url_for
from . import main
from .forms import NameForm
from .. import db
from ..models import User


@main.route('/',methods=['GET','POST'])
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


@main.route('/res')
def res():
	response = make_response('<h1>Response idle</h1>')
	response.set_cookie('answer', '42')
	return response


@main.route('/redirect')
def req():  # �������ֲ��ܺ�redirect() �г�ͻ
	# url_for('username', name='redirect')
	return render_template("user.html", name='Redirect')


@main.route('/user/<name>')
def username(name):
	classmates = ['Michael', 'Bob', 'Tracy']
	return render_template('user.html', name=name, comments=classmates)


@main.route('/bsbase')
def bsbase():
	return render_template("bs_bash.html")
