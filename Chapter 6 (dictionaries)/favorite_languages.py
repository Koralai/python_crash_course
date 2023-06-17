# Make a list of people to take a poll, plus a dictionary of poll results.
# The poll is about people's favorite programming language.

people_to_poll = [
    'jen',
    'helen',
    'phil',
    'andrew',
    'norman',
    'elise',
]

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    'elise': 'java'
}

# Check if each person has taken the poll yet. Send a message in response.

for person in people_to_poll:
    if person in favorite_languages.keys():
        print(f'{person.title()}, thanks for responding to the poll!')
    else:
        print(f'{person.title()}, please consider taking the poll.')