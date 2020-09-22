# 7.4 PIZZA TOPPINGS

pizza_prompt = "\nEnter a pizza topping, "
pizza_prompt += "\nor press quit to exit: "

topping = ""
while topping != 'quit':
    topping = input(pizza_prompt)

    if topping != 'quit':
        print(topping)

# MOVIE TICKETS

movie_prompt = "Enter your age and ill tell you your ticket price: "

while True:
    age = input(movie_prompt)
    age = int(age)
    if age < 4:
        print("tickets free baby")
        break
    elif age > 3 and age < 12:
        print('10 dollars')
        break
    else:
        print('15$')
        break

