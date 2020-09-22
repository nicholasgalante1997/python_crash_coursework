# 6.4 Glossary 2

glossary = {
	'function': 'a block of code that outputs a return value',
	'string': 'characters contained within quotation marks',
	'float': ' a decimaled number',
	'boolean': 'a true or false value',
	'class': 'a defining set of the same type of objects'
}

glossary['ruby'] = 'a superior language'

# iteratinng through a dictionary for key value pairs
for k, v in glossary.items():
	print(f"{k.title()}: {v.lower()}")

# 6.5 Rivers

rivers = {
	'yellow': 'china',
	'mississippi': 'usa',
	'amazon': 'central america'
}

for river, country in rivers.items():
	print(f"{river}, {country} \n")

for r in rivers.keys():
	print(f"{r} is the river \n")

for c in rivers.values():
	print(f"{c} is the country\n")


code_poll = {
	'nick': 'ruby',
	'chase': 'python',
	'steven': 'css',
	'grant': 'java'
}

student_list = ['chaya', 'anthony', 'steven', 'chase', 'nick']

for student in student_list:
	if student in code_poll.keys():
		print(f"Thank you {student} for taking our poll!")
	else:
		print(f"Why dont you take our poll {student}, you little bitch.")

