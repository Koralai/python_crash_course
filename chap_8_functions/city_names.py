def city_country(name, country):
    """Return a city and country, appropriately formatted."""
    city_country_formatted = f'{name.title()}, {country.title()}'
    return city_country_formatted

test_city = city_country('kyiv', 'ukraine')
print(test_city)