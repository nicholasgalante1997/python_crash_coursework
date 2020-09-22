# 8.1 MESSAGE 

def display_message():
    print('this is a function')

display_message()

# 8.2 favorite book

def favorite_book(title):
    print(f"God damn i love that book {title}")

favorite_book('It')

# 8.3 t-shirt 

def make_shirt(size='med', logo='ilovepython3'):
    print(f"Got a {size} shirt, that says {logo}")

# positional 

make_shirt('small', 'github approrpiate logo')

# keyword 

make_shirt(logo='gh appro logo', size='medium')

make_shirt()

# 8.4 desc city

def desc_city(city, country='USA'):
    print(f"{city} is in {country}")


desc_city('Las Vegas', 'Heaven')
desc_city('LA')





