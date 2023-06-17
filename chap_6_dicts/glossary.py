# Create a glossary of Python terms. Print the glossary in alpha order.

glossary = {
    'conditional': 'checks if something is true or false',
    'list': 'a data structure for storing multiple items',
    'dictionary': 'a data structure for storing information in key-value pairs',
    'loop': 'performs repeated tasks',
    'string': 'a data type for written characters',
    'elif': 'a term used in conditionals, combining else and if',
    'index': 'the location of an item in a list',
    'tuple': 'a list that is immutable (cannot change)',
    'slice': 'a piece of a list',
    'list comprehension': 'lets you create a list with only one line of code',
    'key': 'the first part of an item in a dictionary',
    'value': 'the second part of an item in a dictionary',
}

print('Python glossary:\n')
for term, meaning in sorted(glossary.items()): #.items() grabs keys and values
    print(f'{term.title()}: {meaning.capitalize()}.')