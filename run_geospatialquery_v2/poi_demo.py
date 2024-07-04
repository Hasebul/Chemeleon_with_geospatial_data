import googlemaps
import json
from math import sin, cos, sqrt, atan2, radians

gmaps = googlemaps.Client(key='AIzaSyBnsinvIK8T2C8Kv5Q3gKyVWaTMgINDhVw')


def distance(loc1, loc2):
    # approximate radius of earth in km
    R = 6373.0
    lat1= loc1['lat']
    lon1= loc1['lng']
    lat2= loc2['lat']
    lon2= loc2['lng']


    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c
    return distance


def place():
    cur_location = geocode("Radisson Blu Water Garden Hotel, Dhaka")
    places_results = gmaps.places(
        query="Find all the Hospital",
        location=cur_location,
        # region="BD",
        type="Hospital")
    all_poi = places_results["results"]

    for poi in all_poi:
        dist = distance(loc1=poi['geometry']['location'], loc2=cur_location)
        print(f"{poi['name']} has {poi['rating']} rating, where {poi['user_ratings_total']} people give their rating, "
        f"distance from the current location is {dist} km")


def geocode(address):
    geocode_result = gmaps.geocode(address)
    return geocode_result[0]["geometry"]["location"]


if __name__ == "__main__":
    place()

# routes = gmaps.directions(
#             "Sydney",
#             "Melbourne",
#             mode="bicycling",
#             avoid=["highways", "tolls", "ferries"],
#             units="metric",
#             region="us",
#         )
#
# distance_matrix = gmaps.distance_matrix(
#     origins="Sydney",
#     destinations="Melbourne",
#     mode="bicycling",
#     units="metric",
#     region="us",
# )
#
# geocode_result = gmaps.geocode(address)
