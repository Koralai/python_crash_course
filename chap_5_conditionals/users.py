# Loop through a list of usernames and show a special message for admins.

usernames = [
    'harry',
    'admin',
    'lola',
    'sandro',
    'marena'
]

if usernames:                           # Checks if the list is empty or not
    for username in usernames:
        if username.lower() == 'admin':
            print('Hello admin, would you like to see a status report?')
        else:
            print(f"Hi {username.title()}. See what's happening today.")
else:
    print('We need to find some users!')