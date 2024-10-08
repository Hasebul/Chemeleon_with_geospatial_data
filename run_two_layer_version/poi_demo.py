import googlemaps
import json
from math import sin, cos, sqrt, atan2, radians

gmaps = googlemaps.Client(key='AIzaSyBnsinvIK8T2C8Kv5Q3gKyVWaTMgINDhVw')


def distance(loc1, loc2):
    # approximate radius of earth in km
    R = 6373.0
    lat1 = radians(loc1['lat'])
    lon1 = radians(loc1['lng'])
    lat2 = radians(loc2['lat'])
    lon2 = radians(loc2['lng'])


    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c
    return distance


def place():
    cur_location = geocode("IQVIA Corporate, Durham, NC 27703, United States")
    print(cur_location)
    places_results = gmaps.places(
        query="Find all the coffee shop",
        location=cur_location,
        # region="BD",
        type="coffee shop")
    all_poi = places_results["results"]

    for poi in all_poi:
        dist = distance(loc1=poi['geometry']['location'], loc2=cur_location)
        print(f"{poi['name']} has {poi['rating']} rating, where {poi['user_ratings_total']} people give their rating, "
        f"the location distance from current location is {dist} kilometers")


def geocode(address):
    geocode_result = gmaps.geocode(address)
    return geocode_result[0]["geometry"]["location"]


def route():
    origin_location = geocode("Bangladesh University of Engineering and Technology, Dhaka")
    print(origin_location)
    destination_location = geocode("Cumilla Victoria Collage, Bangladesh")
    print(destination_location)
    routes = gmaps.directions(
                origin="Bangladesh University of Engineering and Technology, Dhaka",
                destination="Cumilla Victoria Collage, Bangladesh",
                mode="driving",
                avoid=["highways", "tolls", "ferries"],
                units="metric",
                region="us",
            )
    with open("route.json", "w") as f:
        json.dump(routes, f, indent=4)


def distance():
    distance_matrix = gmaps.distance_matrix(
        origins="Dhaka, Bangladesh",
        destinations="Chittagong, Bangladesh",
        mode="driving",  # "driving”, “walking”, “transit” or “bicycling”
        units="metric",
        region="us",
    )
    with open("distance_matrix.json", "w") as f:
        json.dump(distance_matrix, f, indent=4)


def place_nearby():
    cur_location = geocode("IQVIA Corporate, Durham, NC 27703, United States")
    pleace_nearby = gmaps.places_nearby(location=cur_location, radius=100000, type="Restaurant")
    with open("place_nearby.json", "w") as f:
        json.dump(pleace_nearby, f, indent=4)


if __name__ == "__main__":
    # place()
    route()
    # distance()
    # place_nearby()

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
