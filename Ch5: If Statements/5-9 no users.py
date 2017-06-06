usernames = ['admin', 'adam', 'eve', 'bob', 'alice']

if usernames:
    for username in usernames:
        if 'admin' in username:
            print("Hello admin, would you like to see a status report?")
        else:
            print("Hello", username + ", thank you for logging in!")
else:
    print("we need some users!")
