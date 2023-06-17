# Create several dictionaries with key facts about pets.
# Store the dictionaries in a list.
# Print a statement containing all the info stored for each pet.

# I set things up so I wouldn't have to mess with "a/an" logic.

pet_1 = {
    'species': 'cat',
    'breed': 'Maine coon',
    'color': 'gray',
    'age': 12,
    'sex': 'female',
    'name': 'kristabelle',
    'treat': 'tuna',
}

pet_2 = {
    'species': 'dog',
    'breed': 'terrier',
    'color': 'white',
    'age': 5,
    'sex': 'male',
    'name': 'jojo',
    'treat': 'beef jerky',
}

pet_3 = {
    'species': 'rabbit',
    'breed': 'fuzzy lop',
    'color': 'light brown',
    'age': 7,
    'sex': 'female',
    'name': 'tina',
    'treat': 'iceberg lettuce',
}

pets = [pet_1, pet_2, pet_3]

for pet in pets:
    
    if pet['sex'] == 'female':
        pronoun_1 = 'she'
        pronoun_2 = 'her'
    else:
        pronoun_1 = 'he'
        pronoun_2 = 'him'
        
    print(f"The {pet['species']} {pet['name'].title()} is a "
          f"{pet['color']}, {pet['age']}-year-old {pet['breed']}.\n"
          f"{pronoun_1.capitalize()}'ll love you forever if you "
          f"give {pronoun_2} {pet['treat']}.\n"
          )