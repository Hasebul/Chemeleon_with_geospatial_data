import os
import json
from openai import AzureOpenAI
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo
import googlemaps
from math import sin, cos, sqrt, atan2, radians
gmaps = googlemaps.Client(key='AIzaSyBnsinvIK8T2C8Kv5Q3gKyVWaTMgINDhVw')
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


def place(query: str, location: tuple, region: str, type: str) -> str:
    """
    Returns a string containing information on nearby places based on a query and location.

    Args:
        query (str): The search term to look for nearby places (e.g. "coffee shop", "restaurant").
        location (tuple): The latitude and longitude of the current location in the format (lat, lng).
        region (str): The region code specified as a string, such as "us" or "ca".
        type (str): The type of place to search for, such as "restaurant", "cafe", or "bar".

    Returns:
        str: A string containing information on the nearby places, including the name, rating, number of ratings, and distance from the current location.
    """
    places_results = gmaps.places(
        query=query,
        location=location,
        # region=region,
        type=type
    )
    all_poi = places_results["results"]
    extract_information = f"The following location are the nearest location and all the location has a destination form the current location {location}:\n"
    location = {'lat':location[0], 'lng':location[1]}
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


def directions(origin: str, destination: str, mode: str = None, waypoints: list = None, alternatives: bool = True) -> dict:
    """
    Returns a dictionary containing information on the directions from an origin to a destination.

    Args:
        origin (str): The starting location for the directions.
        destination (str): The destination for the directions.
        mode (str): The mode of transportation to use for the directions, such as "driving", "walking", or "transit".
        waypoints (list): A list of locations to visit along the route.
        alternatives (bool): Whether to return multiple possible routes.

    Returns:
        dict: A dictionary containing information on the directions, including the number of routes and details on each route.
    """
    # origin = "D03 Flame Tree Ridge", destination = "Aster Cedars Hospital, Jebel Ali", mode = "driving", waypoints = None, alternatives = True
    all_routes = gmaps.directions(
        origin=origin, destination=destination, mode=mode, waypoints=waypoints, alternatives=alternatives
    )

    extract_information = {"number of route": len(all_routes)}
    counter = 0
    for route in all_routes:
        counter = counter + 1
        extract_information[f"route_number_{counter}"] = route
    print(extract_information)
    return extract_information


def run_conversation():
    # Initial user message
    messages = [{"role": "user", "content": "Which restaurant is closest to Marina Bay Sands, Singapore?"}]

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
                    region=function_args.get("region"),
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

            else:
                function_response = json.dumps({"error": "Unknown function"})

            messages.append({
                "tool_call_id": tool_call.id,
                "role": "tool",
                "name": function_name,
                "content": function_response,
            })
    else:
        print("No tool calls were made by the model.")

        # Second API call: Get the final response from the model
    final_response = client.chat.completions.create(
        model=deployment_name,
        messages=messages,
    )

    return final_response.choices[0].message.content


# Run the conversation and print the result
print(run_conversation())

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