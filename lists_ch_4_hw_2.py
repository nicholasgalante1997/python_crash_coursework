# 4.3 Counting to 20

for value in range(1, 21):
	print(value)

# 4.4 One Million

var = list(range(1, 1_000_000))

# for item in var:
# 	print(item)

print(min(var))
print(max(var))
print(sum(var))


# odd numbers 1-20 4.6

print(list(range(1, 20, 2)))

# 4.7 threes

threes = list(range(3, 30, 3))
for multiple in threes:
	print(multiple)

# 4.8 cubes
print('Functional Demonstration of a List Comprehension')
cubes = []
for value in range(1, 11):
	cubes.append(value ** 3)

for cube in cubes:
	print(cube)

# 4.9 cube list comprehension
print('List Comprehension')
cube_alt = [value ** 3 for value in range(1, 11)]
for item in cube_alt:
	print(item)

