# This program practices using independent "if" statements.
# Each one is a separate test that should be run.

favorite_fruits = [
    'banana',
    'pineapple',
    'cherries',
    'raspberries',
    'grapes',
    'kiwi',
    'tangelos'
]

if 'kiwi' in favorite_fruits:
    print('You really like kiwi!')
    
if 'oranges' in favorite_fruits:
    print('You really like oranges!')

if 'banana' in favorite_fruits:
    print('You really like bananas!')
    
if 'starfruit' not in favorite_fruits:
    print("You're not a fan of starfruit.")
    
if 'cherries' not in favorite_fruits:
    print("You're not a fan of cherries.")

if 'pineapple' in favorite_fruits and 'kiwi' in favorite_fruits:
    print('You really like tropical fruits!')