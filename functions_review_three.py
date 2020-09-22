# sandwiches 

def cheffingUp(*args):
    sentence = "Ive got a sandwich with "
    for arg in args:
        sentence = sentence + ", " + arg
    return sentence


print(cheffingUp('bacon', 'lettuce', 'tomato'))
print(cheffingUp('ham', 'swiss'))

# user profile 

def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last 
    return user_info


user = build_profile('Kurt', 'Cobain', band='Nirvana', age=27)

print(user)

# cars 

def auto_assembly(manufacturer, model, **kwargs):
    kwargs['manufacturer'] = manufacturer
    kwargs['model'] = model 
    return kwargs 


myCar = auto_assembly('Hyundai', "Elantra", avg_gas_mileage=34, year=2020)
print(myCar)

