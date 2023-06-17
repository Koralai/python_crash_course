# Create a dictionary of cities. Each value is another dictionary
# containing facts about that city. Print a statement describing the
# information that's been stored for each city.

import datetime                     # Python module that gets the current year
from datetime import datetime

cities = {
    'kyiv': {
        'country': 'ukraine',
        'population': '2,884,000',
        'fact': 'it has the deepest metro station in the world',
        'year_founded': 482,
    },
    
    'washington, d.c.': {
        'country': 'the united states',
        'population': '712,000',
        'fact': 'its cherry blossom festival draws visitors from all over the world',
        'year_founded': 1790,
    },
    
    'amsterdam': {
        'country': 'the netherlands',
        'population': '821,000',
        'fact': 'it has more bicycles than people (about 1.33 bikes per person)',
        'year_founded': 1275,
    }
}

for city, info in cities.items():
    current_year = datetime.now().year
    time_since_founding = current_year - info['year_founded']
    
    print(f'{city.title()} is a city in {info["country"].title()} '
          f'with a population of {info["population"]}. '
          f'It was founded {time_since_founding} years ago.\n'
          f'{info["fact"].capitalize()}.\n'
          )