current_users = ['admin', 'adam', 'eve', 'bob', 'alice']
new_users = ['admin', 'adam', 'evelyn', 'bobby', 'ally']

for new_user in new_users:
    if new_user.lower() in current_users.lower():
        print('This username is taken, enter a new one.')
    else:
        print("this username is available, welcome!")
