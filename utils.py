# utils.py

def format_location(location):
    """
    Helper function to format location information for easier matching.
    :param location: dictionary with keys "city", "country"
    :return: formatted string for location (city, country)
    """
    return f"{location['city']}, {location['country']}"

