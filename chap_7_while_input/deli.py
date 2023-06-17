# Create a list of ordered sandwiches and another list to hold finished orders.

sandwich_orders = [
    'tuna', 
    'pastrami',
    'club', 
    'BLT', 
    'pastrami',
    'Italian veggie', 
    'grilled cheese',
    'pastrami',
    ]

finished_sandwiches = []

# Pastrami is unavailable. Remove pastrami from the list of orders.

print('Sorry, the deli has run out of pastrami.\n')

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

# Move remaining sandwiches from the orders list to the finished list.
# Continue doing this until the list of ordered sandwiches is empty.

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f'Your {current_sandwich} sandwich is ready.')
    finished_sandwiches.append(current_sandwich)

# Print the final list of finished sandwiches.

print('\nFinished sandwiches:')
for sandwich in sorted(finished_sandwiches):
    print(sandwich)
    