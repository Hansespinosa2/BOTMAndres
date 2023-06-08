import re
from geopy.geocoders import Nominatim 
from geopy.exc import GeocoderTimedOut

geocoder  = Nominatim(user_agent="My App")

def find_loc(address):
    address = re.sub(" Ste \d+", "", address) # remove suite
    # address = re.sub(",.*,", "", address) # remove city
    if address == 'Missing':
        location = 'No address input'
    else:
        try:
            location = geocoder.geocode(address)
        except GeocoderTimedOut:
            location = "Timeout Error"
    if location is None:
        location = 'Not found by geopy'
    return location

def coords(key):
    return find_long(key), find_lat(key)

def find_lat(address):
    location = find_loc(address)
    if isinstance(location, str):
        return location
    else:
        return round(location.latitude, 6)

def find_long(address):
    location = find_loc(address)
    if isinstance(location, str):
        return location
    else:
        return round(location.longitude, 6)
