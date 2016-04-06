# coding=utf-8
from flask import Flask, render_template
from flask import make_response
from flask.ext.script import Manager
from flask.ext.bootstrap import Bootstrap
from flask.ext.moment import Moment

app = Flask(__name__)
manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)


@app.route('/')
def hello_world():
	return render_template('index.html')


@app.route('/res')
def res():
	response = make_response('<h1>Response idle</h1>')
	response.set_cookie('answer', '42')
	return response


@app.route('/redirect')
def req():  # 函数名字不能喝redirect() 有冲突
	# url_for('username', name='redirect')
	return render_template("user.html",name='Redirect')


@app.route('/user/<name>')
def username(name):
	classmates = ['Michael', 'Bob', 'Tracy']
	return render_template('user.html', name=name, comments=classmates)


@app.route('/bsbase')
def bsbase():
	return render_template("bs_bash.html")

# @app.error_handlers(404)
# def page_not_found(error):
# 	return render_template('404.html'),404






if __name__ == '__main__':
	# manager.run()
	app.run(debug=True, port=35173)
