locations = [
"Copenhagen",
"Amsterdam",
"Madrid",
"London",
"Munich",
"Paris"
]

print(locations)

# use of sorted() function
print(sorted(locations))
# reverse of sorted function
print(sorted(locations, reverse=True))

locations.reverse()
print(locations)

locations.reverse()
print(locations)

locations.sort()
print(locations)

locations.sort(reverse=True)
print(locations)

dinner_guests = [
"JFK",
"Tommy Jefferson",
"Ulysses Grant",
"William Taft"
]

print(f"Oh shit i have {len(dinner_guests)} presidents coming over tonight and im almost out of pot!")

# functions for lists that python comes with

demo = []

demo.insert(0, "this")
demo.append('demo')
demo.insert(1, "is a")
print(demo)

demo.pop()
demo.remove('is a')
demo.append('rocks')
print(demo)


