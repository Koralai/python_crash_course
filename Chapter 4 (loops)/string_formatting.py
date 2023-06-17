# Convert a list of strings to lowercase.

pasta = [
    'Macaroni',
    'SHELLS',
    'lingUINI',
    'Fusilli',
    'spagHETTI',
    'LASAGNE'
]

# This doesn't work. I'm not sure why.

for pasta_type in pasta:
    pasta_type = pasta_type.lower()
print(pasta)

# This works. You have to access a list item with its index, then change it.
# Range is not inclusive, so range(len(list)) gives the indexes you need.

for item in range(len(pasta)): 
    pasta[item] = pasta[item].lower()
print(pasta)