import random
from flask import render_template, url_for, flash, redirect
from flaskblog import app, db
from flaskblog.forms import RegistrationForm, LoginForm, CommandForm
from flaskblog.models import User, Post, Note, LinuxCommand

posts = [
	{
		'author': 'Jacob Peters',
		'title': 'Blog post 1',
		'content': 'First post content',
		'date_posted': 'April 2, 1985'
	},
	{
		'author': 'Jane Doe',
		'title': 'A blog post',
		'content': 'Words for you to read',
		'date_posted': 'July 7, 1941'
	}
]

@app.route('/', methods=['GET', 'POST'])
@app.route('/home')
def home():
	return render_template('home.html', posts=posts)
	
@app.route('/about')
def about():
	return render_template('about.html', title='About')

@app.route('/register', methods=['POST', 'GET'])
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
		flash(f'Account created for {form.username.data}!', 'success')
		return redirect(url_for('home'))
	return render_template('register.html', title='Register', form=form)
	
@app.route('/login', methods=['POST', 'GET'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		if form.email.data == 'admin@blog.com' and form.password.data == 'password':
			flash(f'You have been logged in!', 'success')
			return redirect(url_for('home'))
		else:
			flash(f'Login Unsuccessful. Please check username and password', 'danger')
	return render_template('login.html', title='Login', form=form)
	

@app.route('/rhcsa', methods=['POST', 'GET'])
def rhcsa():
	commands = db.session.query(LinuxCommand.command)
	
	command = LinuxCommand.query.filter_by(command=random.choice(commands.all())[0]).first()
	return render_template('rhcsa.html', title='RHCSA', command=command)
	
@app.route('/rhcsa/command/new', methods=['POST', 'GET'])
def new_command():
	form = CommandForm()
	if form.validate_on_submit():
		command = LinuxCommand(command=form.command.data, description=form.description.data)
		db.session.add(command)
		db.session.commit()
		flash('Your command has been added.', 'success')
		return redirect(url_for('rhcsa'))
	return render_template('new_command.html', title='New Command', form=form)