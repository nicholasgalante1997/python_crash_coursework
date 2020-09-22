#  6.7 people

people = [
{'nick': {'age': 23, 'fav_lang': 'python', 'tired': True}},
{'jimmy': {'age': 23, 'fav_lang': 'ruby', 'tired': False}},
{'rob': {'age': 23, 'fav_lang': 'java', 'tired': True}}
]

for person in people:
	for name, info in person.items():
		print(f"{name}\n{info['age']}\n{info['fav_lang']}")


# favorite places 

favs = {
	'stan': ['denver', 'south park'],
	'kenny': ['dallas', 'atlanta'],
	'cartman': ['munich', 'sierra leone'],
	'kyle': ['boulder', 'montreal']
}

for name, locs in favs.items():
	print(f"{name.title()}:\n")
	for loc in locs:
		print(f"{loc.lower()}")

# cities 

cities = {
	'ny': {'pop': 1_000_000_000, 'country': 'usa', 'fact': 'dirty as fuck'},
	'la': {'pop': 4_000_000_000, 'country': 'usa', 'fact': 'kanye lives here'},
	'lv': {'pop': 9_000_000_000, 'country': 'usa', 'fact': '4$ lobster'}
}

for city, info in cities.items():
	print(f"{city}: pop: {info['pop']}, country: {info['country']}, fact: {info['fact']};")


