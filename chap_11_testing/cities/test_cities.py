from city_functions import get_formatted_city

def test_city_country():
    """Do results like 'London, England' work?"""
    formatted_name = get_formatted_city('london', 'england')
    assert formatted_name == 'London, England'

def test_city_country_population():
    """Do results like 'Kyiv, Ukraine - population 2,884,000' work?"""
    formatted_name = get_formatted_city('kyiv', 'ukraine', 2884000)
    assert formatted_name == 'Kyiv, Ukraine - Population 2,884,000'
