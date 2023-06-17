# Create a few dictionaries with key facts about a person.
# Store the dictionaries in a list.
# Print everything known about each person.

person_1 = {
    'first': 'sasha',
    'last': 'cohen',
    'age': 38,
    'location': 'newport beach',
    'olympic_medal': 'silver',
}

person_2 = {
    'first': 'michelle',
    'last': 'kwan',
    'age': 42,
    'location': 'belize',
    'olympic_medal': 'bronze',
}

person_3 = {
    'first': 'kristi',
    'last': 'yamaguchi',
    'age': 51,
    'location': 'california',
    'olympic_medal': 'gold',
}

people = [person_1, person_2, person_3]

for person in people:
    print(f'{person["first"].title()} {person["last"].title()}:'
          f'\n\tAge: {person["age"]}'
          f'\n\tLocation: {person["location"].title()}'
          f'\n\tHighest Olympic medal: {person["olympic_medal"].title()}'
          )