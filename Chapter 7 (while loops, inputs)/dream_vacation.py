# Create a dictionary to hold user data as it is created.

dream_vacations = {}

# Create a flag to track whether the poll should continue.

polling = True

# Ask users for their name and where they'd like to visit.

while polling == True:
    name = input('\nWhat is your name? ')
    response = input('If you could visit one place in the world, '
                    'where would you go? ')
    
    # Store this info in the dictionary.
    
    dream_vacations[name] = response
    
    # Check if the poll should continue. If not, 
    # switch the flag to exit the loop.
    
    ask_to_continue = input('Would someone else like to take the poll? '
                            'yes/no ')
    if ask_to_continue.lower() == 'no':
        polling = False

# Print the gathered information about people's dream vacations.

for person, place in dream_vacations.items():
    print(f'\n{person.title()} would like to visit {place}.')