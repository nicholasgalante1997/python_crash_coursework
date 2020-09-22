usernames = ['Admin', 'Nick', "NickG", "Sean", "Craig"]

if usernames:
	for user in usernames:
		if user == "Admin":
			print(f"Hello {user}, would you like a status report?")
		else:
			print(f"Hello {user}")
else:
	print('Man we need to find some users')

current_users = ['Cool_User', "Shy_User", "Drunk_User", "Annoying_User", "High_User"]

new_users = ['dope_user', 'Cool_User', 'Fun_User']

case_sensitive_current_users = []
for current_user in current_users:
	case_sensitive_current_users.append(current_user.lower())

for new_user in new_users:
	if new_user.lower() in case_sensitive_current_users:
		print('that name has been taken')
	else:
		current_users.append(new_user)

print(current_users)

# ordinal numbers

nums = list(range(1, 10))
for num in nums:
	if num == 1:
		print('1st')
	elif num == 2:
		print('2nd')
	elif num == 3:
		print('3rd')
	else:
		print(f"{num}th")




