def describe_city(name, country='the United States'):
    """Display a simple message about a city and where it's located."""
    print(f'{name.title()} is in {country.title()}.')

describe_city('portland')       # USA's the default country, can leave unstated
describe_city(name='indianapolis')
describe_city(name='bangkok', country='thailand')