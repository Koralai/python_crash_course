rivers = {
    'dnieper': 'ukraine',
    'mississippi': 'the united states',
    'ganges': 'india',
    'colorado': 'the united states',
    'amazon': 'brazil',
}

for river, country in rivers.items():
    print(f'The {river.title()} river runs through {country.title()}.')

print('\nRivers included in this dictionary:')
for river in sorted(rivers.keys()):
    print(f'{river.title()}')

print('\nCountries included in this dictionary:')
for country in sorted(set(rivers.values())):  # set() for a list of unique values
    print(f'{country.title()}')