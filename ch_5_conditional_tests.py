# conditional tests in python

favorite_book = 'Python Crash Course'

print(favorite_book == 'Python Crash Course')

print(favorite_book == 'Eloquent Javascript')

bookshelf = [
"Pragmatic Ruby",
"The Well Grounded Rubyist",
"Eloquent Javascript",
"Pro React 16",
"Python Crash Course"
]

# use of in and use of not in
print("Pragmatic Ruby" in bookshelf)
print("CSS and HTML" not in bookshelf)


for book in bookshelf:
	if book == favorite_book:
		print(f"Oh shit, {book} is my shit!")
	else:
		print(f"{book} is in my library, its like not bad.")

# and 

print(2 < 5 and 3 > 2)
print(2 > 5 and 3 > 2)
print(2 > 5 or 3 > 2)
print(2 > 5 or 3 < 2)

