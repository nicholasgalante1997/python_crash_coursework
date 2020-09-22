# 7.1 rental car

car_type = input('What kind of car would you like? ')
print(f"Lemme see if i can find a {car_type} for you, hang on bro.")

# 7.2 restaurant seating

party = input('How many in your party today?')
party = int(party)

if party > 8:
    print('Im sorry theres going to be a wait')
else:
    print('right this way')

# 7.3 multiples of 10

num = input('give me a num mf')
num = int(num)
if num % 10 == 0:
    print(f"yeah buddy {num} is an interval of 10")
else:
    print(f"it would appear that {num} is not an interval of 10, bummer")







