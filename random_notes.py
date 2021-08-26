import random
from flaskblog import db
from flaskblog.models import Note
from faker import Faker

fake = Faker()

commands = [
	'df',
	'cron',
	'chmod',
	'chown',
	'mount',
	'useradd',
	'chage'
]

file_args = [
	'PASS_MAX_DAYS',
	'PASS_MIN_DAYS',
	'PASS_WARN_AGE'
]

cli_args = [
	'-E',
	'-l',
	'-m',
	'-M',
	'-W',
	'-I'
]

for _ in range(10):
	cmd = random.choice(commands)
	
	cli_file = fake.random_elements(elements=(0, 1), unique=True, length=2)
	
	comments = fake.paragraphs(nb=1)
	
	if cli_file[0]:
		arg = random.choice(cli_args)
		example = f'{cmd} {arg} {fake.word()}'
	else:
		arg = random.choice(file_args)
		example = f'{arg} - {comments[0]}'
	
	note = Note(
					command=f'{cmd}', 
					cli=cli_file[0], 
					file=cli_file[1], 
					argument=f'{arg}', 
					example=f'{example}', 
					comments=f'{comments[0]}'
				)
	db.session.add(note)
	db.session.commit()
