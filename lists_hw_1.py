deceased_guests = ["Kurt Cobain", "Amy Winehouse", 'John Gardner', 'Chris Farley']

print(f"Sucks you can't make it {deceased_guests[0]}!")

deceased_guests.remove('Kurt Cobain')

# for guest in deceased_guests:
# 	print(f"Welcome to the party {guest}")


deceased_guests.insert(0, "John F Kennedy")
deceased_guests.insert(2, "Jesus Christ")
deceased_guests.append('Ted Bundy')


for guest in deceased_guests:
	print(f"Welcome to the party {guest}")


print(len(deceased_guests))

jfk = deceased_guests.pop(0)
amy = deceased_guests.pop(0)
jesus = deceased_guests.pop(0)

print(deceased_guests)

print(f"Sorry we couldnt fit you guys, {jfk}, {amy}, {jesus}")




