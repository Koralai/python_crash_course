# Create a dictionary that contains people and their favorite places.
# Print each person's name and their favorite places.

favorite_places = {
    'anna': ['kyiv', 'warsaw', 'prague'],
    'joseph': ['hawaii', 'pensacola', 'hilton head'],
    'howie': ['washington, d.c.', 'philadelphia', 'boston'],
    'lacey': ['santa fe', 'denver', 'miami']
}

for person, places in favorite_places.items():
    print(f"{person.title()}'s favorite places:")
    for place in places:
        print(f'\t{place.title()}')