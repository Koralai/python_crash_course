# Declare a person's age.

age = 35

# Find a term for their stage of life, based on their age.

if age < 2:
    life_stage = 'baby'
elif age < 4:
    life_stage = 'toddler'
elif age < 13:
    life_stage = 'kid'
elif age < 20:
    life_stage = 'teenager'
elif age < 65:
    life_stage = 'adult'
elif age >= 65:
    life_stage = 'elder'    

# Determine the article (a/an) that matches the word for their stage of life.
# If the first letter of the word is a vowel, the article is "an."

if life_stage[0].lower() in ['a', 'e', 'i', 'o', 'u']:
    article = 'an'
else:
    article = 'a'

# Print a statement about what stage of life the person is in.

print(f'You are {article} {life_stage}.')
