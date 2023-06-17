# Check if potential new usernames are available (case insensitive).

current_users = [
    'Plato',
    'Socrates',
    'hypatia',
    'kant',
    'HUME'
]

new_users = [
    'socrates',
    'foote',
    'hume',
    'Aristotle',
    'seneca'
]

# Make a copy of the list of current users in all lowercase.

current_users_formatted = []
for current_user in current_users:
    current_users_formatted.append(current_user.lower())
    
# Check if a new username exists and if it's already taken.

if new_users:
    for new_user in new_users:
        if new_user.lower() in current_users_formatted:
            print(f'Sorry, the username {new_user} is already taken.') 
        else:
            print(f'The username {new_user} is available.')                       
else:
    print('No new users at this time.')