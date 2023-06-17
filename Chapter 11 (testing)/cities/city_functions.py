def get_formatted_city(city, country, population=None):
    if population:
        formatted_name = f"{city}, {country} - population {population:,}"
    else:
        formatted_name = f"{city}, {country}"
    return formatted_name.title()
