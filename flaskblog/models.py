from flaskblog import db
from datetime import datetime

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(20), unique=True, nullable=False)
	email = db.Column(db.String(120), unique=True, nullable=False)
	image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
	password = db.Column(db.String(60), nullable=False)
	posts = db.relationship('Post', backref='author', lazy=True)
	
	def __repr__(self):
		return f"User('{self.username}', '{self.email}', '{self.image_file}')"
		
		
class Post(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(100), nullable=False)
	date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
	content = db.Column(db.Text, nullable=False)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
	
	def __repr__(self):
		return f"Post('{self.title}', '{self.date_posted}')"


class Note(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	command = db.Column(db.String(20), nullable=False)
	cli = db.Column(db.Boolean, nullable=False)
	file = db.Column(db.Boolean, nullable=False)
	argument = db.Column(db.String(20), nullable=False)
	example = db.Column(db.Text, nullable=False)
	comments = db.Column(db.Text, nullable=False)
	
	def __repr__(self):
		return f"Note('{self.command}', '{self.argument}', '{self.comments}')"
		
class LinuxCommand(db.Model):
	__tablename__ = 'linuxcommand'
	id = db.Column(db.Integer, primary_key=True)
	command = db.Column(db.String(20), nullable=False, unique=True)
	description = db.Column(db.Text, nullable=False)
	options = db.relationship('CommandOption', backref='options', lazy=True)
	arguments = db.relationship('CommandArgument', backref='arguments', lazy=True)
	configs = db.relationship('CommandConfig', backref='configs', lazy=True)
	
	def __repr__(self):
		return f"LinuxCommand('{self.command}, {self.description}')"
		
class CommandOption(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	option_short = db.Column(db.String(10), nullable=False)
	option_long = db.Column(db.String(10), nullable=False)
	argument = db.Column(db.String(20), nullable=True)
	description = db.Column(db.Text, nullable=False)
	command_id = db.Column(db.Integer, db.ForeignKey('linuxcommand.id'), nullable=False)
	
	def __repr__(self):
		return f"CommandOption('{self.option_short}, {self.option_long}, {self.description}')"
		
class CommandArgument(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	argument = db.Column(db.String(20), nullable=False)
	description = db.Column(db.Text, nullable=False)
	command_id = db.Column(db.Integer, db.ForeignKey('linuxcommand.id'), nullable=False)
	
	def __repr__(self):
		return f"CommandArgument('{self.argument}, {self.description}'')"
		
class CommandConfig(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(20), nullable=False)
	path = db.Column(db.String(100), nullable=False)
	description = db.Column(db.Text, nullable=False)
	command_id = db.Column(db.Integer, db.ForeignKey('linuxcommand.id'), nullable=False)
	
	def __repr__(self):
		return f"CommandConfig('{self.name}, {self.path}, {self.description}')"