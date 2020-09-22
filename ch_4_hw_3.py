# 4.10

gen_list = list(range(1, 11))

print(f"The first three items in the list are {gen_list[:3]}")

print(f"The middle of the list has {gen_list[3:7]}")

print(f"The last items are {gen_list[-3:]}")

restuarants = ["McDonald's", "Kotobuki", "Blackstone"]

restuarants_copy = restuarants[:]

print(restuarants_copy)

restuarants.append('Thai Time')
restuarants_copy.append('Bolonial')

print(restuarants)
print(restuarants_copy)
