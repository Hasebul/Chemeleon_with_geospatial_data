import os
import json
from openai import AzureOpenAI
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo
import googlemaps
from math import sin, cos, sqrt, atan2, radians

gmaps = googlemaps.Client(key='AIzaSyA2g27UGq_N5DktbQXsxdf8qDyNSsPUTLo')
# Initialize the Azure OpenAI client
client = AzureOpenAI(
    azure_endpoint="https://llms-eus2.openai.azure.com/",
    api_key="c7d579ff57394bf98d6da39f9c96bca5",
    api_version="2024-05-01-preview",
    azure_deployment="gpt-35-turbo-0125",
)

# Provide the model deployment name you want to use for this example

deployment_name = "gpt-35-turbo-0125"

# Simplified weather data
WEATHER_DATA = {
    "tokyo": {"temperature": "10", "unit": "celsius"},
    "san francisco": {"temperature": "72", "unit": "fahrenheit"},
    "paris": {"temperature": "22", "unit": "celsius"}
}

# Simplified timezone data
TIMEZONE_DATA = {
    "tokyo": "Asia/Tokyo",
    "san francisco": "America/Los_Angeles",
    "paris": "Europe/Paris"
}


def get_travel_info(origin_address: str, destination_address: str, mode: str = "driving"):
    """
    Returns the travel time and distance between two addresses.

    Parameters:
        origin_address (str): The starting address of the journey.
        destination_address (str): The destination address of the journey.
        mode (str): The driving mood of the journey

    Returns:
        tuple: A tuple containing the travel time and distance in text format.
    """
    now = datetime.now()
    directions_result = gmaps.directions(origin=origin_address,
                                         destination=destination_address,
                                         mode=mode,
                                         departure_time=now)
    travel_time_text = directions_result[0]['legs'][0]['duration']['text']
    travel_distance_text = directions_result[0]['legs'][0]['distance']['text']
    return travel_time_text, travel_distance_text


def get_place_info(location_address):
    """
    Returns the details of a place, including its name, address, rating, types,
    opening hours, and whether it is currently open.

    Parameters:
        location_address (str): The address or name of the location to search for.

    Returns:
        dict: A dictionary containing the place details.
    """
    place_result = gmaps.places(location_address)
    if len(place_result['results']) == 0:
        print("No results found for location", location_address)
    else:
        place_id = place_result['results'][0]['place_id']
    place_result = gmaps.place(place_id)
    if len(place_result['result']) == 0:
        print("No results found for location", location_address)
    else:
        place = place_result['result']
        name = place['name']
        address = place['formatted_address']
        rating = place['rating'] if 'rating' in place else 'N/A'
        types = place['types']
        if "current_opening_hours" in place.keys():
            opening_hours = place["current_opening_hours"]
        elif "opening_hours" in place.keys():
            opening_hours = place["opening_hours"]
        else:
            opening_hours = {}
        is_open_now = opening_hours['open_now'] if 'open_now' in opening_hours else 'N/A'
        weekdays_opening_hours = opening_hours["weekday_text"] if opening_hours else 'N/A'
        place_info = {
            'name': name,
            'address': address,
            'rating': rating,
            'types': types,
            'is_open_now': is_open_now,
            'weekdays_opening_hours': weekdays_opening_hours,
        }
        return place_info


def distance(loc1: dict, loc2: dict) -> float:
    """
    Returns the distance between two locations in kilometers.

    Args:
        loc1 (dict): A dictionary containing the latitude and longitude coordinates of the first location in the format {"lat": lat, "lng": lng}.
        loc2 (dict): A dictionary containing the latitude and longitude coordinates of the second location in the format {"lat": lat, "lng": lng}.

    Returns:
        float: The distance between the two locations in kilometers.
    """
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


def place(query: str, location: tuple, type: str) -> str:
    """
    Returns a string containing information on nearby places based on a query and location.

    Args:
        query (str): The search term to look for nearby places (e.g. "coffee shop", "restaurant").
        location (tuple): The latitude and longitude of the current location in the format (lat, lng).
        type (str): The type of place to search for, such as "restaurant", "cafe", or "bar".

    Returns:
        str: A string containing information on the nearby places, including the name, rating, number of ratings, and distance from the current location.
    """
    places_results = gmaps.places(
        query=query,
        location=location,
        type=type
    )
    all_poi = places_results["results"]
    extract_information = f"The following location are the nearest location and all the location has a destination form the current location {location}:\n"
    location = {'lat': location[0], 'lng': location[1]}
    for poi in all_poi:
        dist = distance(loc1=poi['geometry']['location'], loc2=location)
        rating = poi['rating'] if 'rating' in poi.keys() else 0
        total_user = poi['user_ratings_total'] if 'user_ratings_total' in poi.keys() else 0
        extract_information = extract_information + f"{poi['name']} has {rating} rating," + f"where {total_user} people give their rating, " + f"the location distance from current location is {dist} kilometers\n"
    return extract_information


def geocode(address: str) -> tuple:
    """
    Returns a tuple containing the latitude and longitude coordinates for a given address.

    Args:
        address (str): The address to geocode.

    Returns:
        tuple: A tuple containing the latitude and longitude coordinates in the format (lat, lng).
    """
    geocode_result = gmaps.geocode(address)
    return geocode_result[0]["geometry"]["location"]


def directions(origin: str, destination: str, mode: str = None, waypoints: list = None,
               alternatives: bool = True) -> str:
    """
    Returns a dictionary containing information on the directions from an origin to a destination.

    Args:
        origin (str): The starting location for the directions.
        destination (str): The destination for the directions.
        mode (str): The mode of transportation to use for the directions, such as "driving", "walking", or "transit".
        waypoints (list): A list of locations to visit along the route.
        alternatives (bool): Whether to return multiple possible routes.

    Returns:
        str: A string containing information on the directions, including the number of routes and details on each route.
    """
    # origin = "D03 Flame Tree Ridge", destination = "Aster Cedars Hospital, Jebel Ali", mode = "driving", waypoints = None, alternatives = True
    all_routes = gmaps.directions(
        origin=origin, destination=destination, mode=mode, waypoints=waypoints, alternatives=alternatives
    )
    extract_information = f"There are total {len(all_routes)} routes from {origin} to {destination}. The route information is provided below:\n\n"
    num = 0
    for route in all_routes:
        num += 1
        dist = route["legs"][0]["distance"]["text"]
        duration = route["legs"][0]["duration"]["text"]
        via = route["summary"]
        extract_information += f"Route {num}: VIA {via} will cover {dist} in {duration}\nDetails steps are provided below: \n"
        for step in route["legs"][0]["steps"]:
            s_dist = step["distance"]["text"]
            s_duration = step["duration"]["text"]
            html_content = step["html_instructions"]
            soup = BeautifulSoup(html_content, 'html.parser')
            # Extract the text from the HTML content
            s_text = soup.get_text()
            extract_information += f"{s_text} will cover {s_dist} in {s_duration} \n"
        extract_information += "\n"
    return extract_information


def trip(current_location: str, visiting_places: list[str], travel_mode: str = "driving"):
    """
    Returns a string containing the location information and travel time and distance between the locations.

    Parameters:
        current_location (str): The starting location of the trip.
        visiting_places (list): A list of locations to visit.
        travel_mode (str): The mode of travel, defaults to "driving".

    Returns:
        str: A string containing the location information and travel time and distance between the locations.
    """
    all_locations = [current_location] + visiting_places
    place_info_str = 'All Location Info: \n'
    for loc in all_locations:
        place_info_str += loc + ' \n'
        place_info = get_place_info(loc)
        place_info_str += f"Name: {place_info['name']}\nAddress: {place_info['address']}\nRating: {place_info['rating']}\nTypes: {', '.join(place_info['types'])}\nIs Open Now: {place_info['is_open_now']}\nWeekday Opening Hours:\n"
        if place_info['weekdays_opening_hours'] == 'N/A':
            place_info_str += f"- {'Unknown'}\n"
        else:
            for weekday_open_hours in place_info['weekdays_opening_hours']:
                place_info_str += f"- {weekday_open_hours}\n"
    for i in range(0, len(all_locations)):
        for j in range(0, len(all_locations)):
            origin = all_locations[i]
            destination = all_locations[j]
            if origin == destination:
                continue
            travel_time_text, travel_distance_text = get_travel_info(origin, destination, travel_mode)
            place_info_str += f"The travel time(distance) from {origin} to {destination} is {travel_time_text} ({travel_distance_text})\n"
    # print(place_info_str)
    return place_info_str


def run_conversation(query):
    # Initial user message
    messages = [
        {"role": "system",
         "content": "As a system prompt, you are an agent that can direct the corresponding function call based on the user's question and retrieve the requested information. Your task is to fetch the information and provide it to the user. You are not expected to answer the question directly. The user will provide you with a question, and your role is to retrieve the relevant information using the appropriate function."},
        {"role": "user",
         "content": query}]

    # Define the functions for the model
    tools = [
        {
            "type": "function",
            "function": {
                "name": "place",
                "description": "Get information on nearby places based on a query and location",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "query": {
                            "type": "string",
                            "description": "The search term to look for nearby places (e.g. 'coffee shop', 'restaurant')",
                        },
                        "location": {
                            "type": "array",
                            "items": {
                                "type": "number"
                            },
                            "description": "The latitude and longitude of the current location in the format [lat, lng].",
                        },
                        "region": {
                            "type": "string",
                            "description": "The region code specified as a string, such as 'us' or 'ca'.",
                        },
                        "type": {
                            "type": "string",
                            "description": "The type of place to search for, such as 'restaurant', 'cafe', or 'bar'.",
                        },
                    },
                    "required": ["query", "location", "type"],
                },
            },
        },
        {
            "type": "function",
            "function": {
                "name": "directions",
                "description": "Get information on directions from an origin to a destination",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "origin": {
                            "type": "string",
                            "description": "The starting location for the directions.",
                        },
                        "destination": {
                            "type": "string",
                            "description": "The destination for the directions.",
                        },
                        "mode": {
                            "type": "string",
                            "description": "The mode of transportation to use for the directions, such as 'driving', 'walking', or 'transit'.",
                        },
                        "waypoints": {
                            "type": "array",
                            "items": {
                                "type": "string"
                            },
                            "description": "A list of locations to visit along the route.",
                        },
                        "alternatives": {
                            "type": "boolean",
                            "description": "Whether to return multiple possible routes.",
                        },
                    },
                    "required": ["origin", "destination"],
                },
            },
        },
        {
            "type": "function",
            "function": {
                "name": "trip",
                "description": "Returns a string containing the location information and travel time and distance between the locations.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "current_location": {
                            "type": "string",
                            "description": "The starting location of the trip."
                        },
                        "visiting_places": {
                            "type": "array",
                            "items": {
                                "type": "string"
                            },
                            "description": "A list of locations to visit."
                        },
                        "travel_mode": {
                            "type": "string",
                            "description": "The mode of travel, defaults to 'driving'.",
                            "enum": [
                                "driving",
                                "walking",
                                "bicycling",
                                "transit"
                            ]
                        }
                    },
                    "required": [
                        "current_location",
                        "visiting_places"
                    ]
                },
                "returns": {
                    "type": "string",
                    "description": "A string containing the location information and travel time and distance between the locations."
                }
            }
        }
    ]

    # First API call: Ask the model to use the functions
    response = client.chat.completions.create(
        model=deployment_name,
        messages=messages,
        tools=tools,
        tool_choice="auto",
    )

    # Process the model's response
    response_message = response.choices[0].message
    messages.append(response_message)

    print("Model's response:")
    print(response_message)

    # Handle function calls
    if response_message.tool_calls:
        for tool_call in response_message.tool_calls:
            function_name = tool_call.function.name
            function_args = json.loads(tool_call.function.arguments)
            print(f"Function call: {function_name}")
            print(f"Function arguments: {function_args}")

            if function_name == "place":
                function_response = place(
                    query=function_args.get("query"),
                    location=function_args.get("location"),
                    # region=function_args.get("region"),
                    type=function_args.get("type")
                )

            elif function_name == "directions":
                function_response = directions(
                    origin=function_args.get("origin"),
                    destination=function_args.get("destination"),
                    mode=function_args.get("mode"),
                    waypoints=function_args.get("waypoints"),
                    alternatives=function_args.get("alternatives")
                )

            elif function_name == "trip":
                function_response = trip(
                    current_location=function_args.get("current_location"),
                    visiting_places=function_args.get("visiting_places"),
                    travel_mode=function_args.get("travel_mode"),
                )

            else:
                function_response = json.dumps({"error": "Unknown function"})

            # print(function_response)
            messages.append({
                "tool_call_id": tool_call.id,
                "role": "tool",
                "name": function_name,
                "content": function_response,
            })
    else:
        print("No tool calls were made by the model.")

        # Second API call: Get the final response from the model
    # final_response = client.chat.completions.create(
    #     model=deployment_name,
    #     messages=messages,
    # )

    # return final_response.choices[0].message.content
    return function_response


if __name__ == "__main__":
    # current_loc = 'Khaosan Tokyo Origami in Asakusa, Tokyo'
    # visiting_place_list = ['Sensō-ji Temple', 'Shibuya Crossing', ' Ueno Park', ' Tokyo Skytree']
    # place_info_str= trip(current_loc, visiting_place_list)
    # print(place_info_str)
    # Run the conversation and print the result
    print(run_conversation())
    # place = directions(origin="Obelisco de Buenos Aires", destination="Caminito in La Boca")
    # print(place)

# Run the conversation and print the result
# print(run_conversation())

# def get_current_weather(location, unit=None):
#     """Get the current weather for a given location"""
#     print(f"get_current_weather called with location: {location}, unit: {unit}")
#     location_lower = location.lower()
#
#     for key in WEATHER_DATA:
#         if key in location_lower:
#             print(f"Weather data found for {key}")
#             weather = WEATHER_DATA[key]
#             return json.dumps({
#                 "location": location,
#                 "temperature": weather["temperature"],
#                 "unit": unit if unit else weather["unit"]
#             })
#
#     print(f"No weather data found for {location_lower}")
#     return json.dumps({"location": location, "temperature": "unknown"})
#
#
# def get_current_time(location):
#     """Get the current time for a given location"""
#     print(f"get_current_time called with location: {location}")
#     location_lower = location.lower()
#
#     for key, timezone in TIMEZONE_DATA.items():
#         if key in location_lower:
#             print(f"Timezone found for {key}")
#             current_time = datetime.now(ZoneInfo(timezone)).strftime("%I:%M %p")
#             return json.dumps({
#                 "location": location,
#                 "current_time": current_time
#             })
#
#     print(f"No timezone data found for {location_lower}")
#     return json.dumps({"location": location, "current_time": "unknown"})
#
#
# def run_conversation():
#     # Initial user message
#     messages = [{"role": "user", "content": "What's the weather and current time in San Francisco, Tokyo, and Paris?"}]
#
#     # Define the functions for the model
#     tools = [
#         {
#             "type": "function",
#             "function": {
#                 "name": "get_current_weather",
#                 "description": "Get the current weather in a given location",
#                 "parameters": {
#                     "type": "object",
#                     "properties": {
#                         "location": {
#                             "type": "string",
#                             "description": "The city name, e.g. San Francisco",
#                         },
#                         "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]},
#                     },
#                     "required": ["location"],
#                 },
#             }
#         },
#         {
#             "type": "function",
#             "function": {
#                 "name": "get_current_time",
#                 "description": "Get the current time in a given location",
#                 "parameters": {
#                     "type": "object",
#                     "properties": {
#                         "location": {
#                             "type": "string",
#                             "description": "The city name, e.g. San Francisco",
#                         },
#                     },
#                     "required": ["location"],
#                 },
#             }
#         }
#     ]
#
#     # First API call: Ask the model to use the functions
#     response = client.chat.completions.create(
#         model=deployment_name,
#         messages=messages,
#         tools=tools,
#         tool_choice="auto",
#     )
#
#     # Process the model's response
#     response_message = response.choices[0].message
#     messages.append(response_message)
#
#     print("Model's response:")
#     print(response_message)
#
#     # Handle function calls
#     if response_message.tool_calls:
#         for tool_call in response_message.tool_calls:
#             function_name = tool_call.function.name
#             function_args = json.loads(tool_call.function.arguments)
#             print(f"Function call: {function_name}")
#             print(f"Function arguments: {function_args}")
#
#             if function_name == "get_current_weather":
#                 function_response = get_current_weather(
#                     location=function_args.get("location"),
#                     unit=function_args.get("unit")
#                 )
#             elif function_name == "get_current_time":
#                 function_response = get_current_time(
#                     location=function_args.get("location")
#                 )
#             else:
#                 function_response = json.dumps({"error": "Unknown function"})
#
#             messages.append({
#                 "tool_call_id": tool_call.id,
#                 "role": "tool",
#                 "name": function_name,
#                 "content": function_response,
#             })
#     else:
#         print("No tool calls were made by the model.")
#
#         # Second API call: Get the final response from the model
#     final_response = client.chat.completions.create(
#         model=deployment_name,
#         messages=messages,
#     )
#
#     return final_response.choices[0].message.content
#
#
# # Run the conversation and print the result
# print(run_conversation())
