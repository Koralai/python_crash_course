# Get info from the user on how many people are in their dinner party.
# Print a message based on the size of this group.

group = input('How many people are in your dinner group? ')
group = int(group)  # Convert the user input to an integer

if group > 8:
    print('Your wait will be around 30 minutes.')
else:
    print('Your table is ready!')