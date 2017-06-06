usernames = ['admin', 'adam', 'eve', 'bob', 'alice']

for username in usernames:
    if 'admin' in username:
        print("Hello admin, would oyu like to see a status report?")
    else:
        print("Hello", username + ", thank you for logging in")
