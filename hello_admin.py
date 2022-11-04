current_users = ['Amanda', 'FRANK', 'MEllie', 'Deborah', 'Shortie']
current_users_lower = []
new_users = ['amANda', 'mellIe', 'Erica', 'Bell', 'Duke']
for current_user in current_users:
	current_users_lower.append(current_user.lower())
for new_user in new_users:
	if new_user.lower() in current_users_lower:
		print("Sorry, you will have to choose a different username")
	else:
		print("That username is available")
