# Create a dictionary that contains people and their favorite numbers.
# Print each person's name and their favorite numbers.

# All of the values are lists, even when there is only one item.
# Otherwise, the code wouldn't work.

favorite_numbers = {
    'coco': [8, 16, 40],
    'lana': [2, 3, 5, 7, 11, 13],
    'howard': [99],                 # One number only, still a list
    'clayton': [42],
    'mary': [88, 92, 47, 51],
}

for person, numbers in favorite_numbers.items():
    print(f"{person.title()}'s favorite numbers:")
    for number in numbers:
        print(f'\t{number}')