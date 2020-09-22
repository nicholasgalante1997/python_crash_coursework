#  city names 

def city_country(city, country):
    return f"{city},{country}"

print(city_country('NYC', 'USA'))

# album 

def make_album(artist, title, num_of_songs=None):
    if num_of_songs:
        return {'artist': artist, 'album': title, 'duration': num_of_songs}
    else:
        return {'artist': artist, 'album': title}

print(make_album('Amy Winehouse', 'Back to Black', 13))
print(make_album('Kendrick Lamar', 'To Pimp a Butterfly'))

# while loops and breaks

while True:
    art = input("Enter an Artist: ")
    alb = input("Enter an Album\nPress q at any time to quit ")
    if art == 'q':
        break
    elif alb == 'q':
        break 
    else:
        print(make_album(art, alb))

# messages 

messages = ['Hey', "hey", 'heyyyyyy', 'no']

def show_msgs(messages):
    for message in messages:
        print(message)

show_msgs(messages)

# destructive list modification 
new_msgs = ['a', 'e', 'i', 'o', 'u']
sent_msgs = []

def sending_msgs(messages, sent_messages):
    while messages:
        current = messages.pop()
        sent_messages.append(current)
    for msg in sent_messages:
        print(msg)


# non destructive using copy 

sending_msgs(new_msgs[:], sent_msgs)

print(new_msgs, sent_msgs)

