import googlemaps
import json



def distance(loc1, loc2):
    # approximate radius of earth in km
    R = 6373.0
    lat1 = loc1['lat']
    lon1 = loc1['lng']
    lat2 = loc2['lat']
    lon2 = loc2['lng']
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = R * c
    return distance


def place(query, location, region, type):
    places_results = gmaps.places(
        query=query,
        location=location,
        region=region,
        type=type
    )
    print(places_results)
    all_poi = places_results["results"]
    extract_information = ""
    for poi in all_poi:
        dist = distance(loc1=poi['geometry']['location'], loc2=location)
        extract_information = extract_information + f"{poi['name']} has {poi['rating']} rating," + f"where {poi['user_ratings_total']} people give their rating, " + f"distance from the current location is {dist} km \n"
    return extract_information


def gpt():
    import os
    import requests
    import base64

    # Configuration
    # API_KEY = "01488083a8d243e684bd48a39152d90a"
    # # API_KEY = "YOUR_API_KEY"
    # # IMAGE_PATH = "YOUR_IMAGE_PATH"
    # # encoded_image = base64.b64encode(open(IMAGE_PATH, 'rb').read()).decode('ascii')
    # headers = {
    #     "Content-Type": "application/json",
    #     "api-key": API_KEY,
    # }
    API_KEY = "154bfc83018f41f19341d76cefe5d95c"
    # API_KEY = "YOUR_API_KEY"
    # IMAGE_PATH = "YOUR_IMAGE_PATH"
    # encoded_image = base64.b64encode(open(IMAGE_PATH, 'rb').read()).decode('ascii')
    headers = {
        "Content-Type": "application/json",
        "api-key": API_KEY,
    }

    # Payload for the request
    # payload = {
    #     "messages": messages,
    #     "temperature": 0.7,
    #     "top_p": 0.95,
    #     "max_tokens": 1000
    # }
    # GPT-35-TURBO-0125
    ENDPOINT = "https://qcri-llm-rag-3.openai.azure.com/openai/deployments/gpt-35-turbo/chat/completions?api-version=2023-03-15-preview"

    # Payload for the request
    payload = {
        "messages": [
            {
                "role": "system",
                "content": [
                    {
                        "type": "text",
                        "text": "You are an AI assistant that helps people find information. What is the capital of dhaka"
                    }
                ]
            }
        ],
        "temperature": 0.7,
        "top_p": 0.95,
        "max_tokens": 800
    }

    # ENDPOINT = "https://qcri-llm-rag-4.openai.azure.com/openai/deployments/GPT-4o/chat/completions?api-version=2024-02-15-preview"

    # Send request
    try:
        response = requests.post(ENDPOINT, headers=headers, json=payload)
        response.raise_for_status()  # Will raise an HTTPError if the HTTP request returned an unsuccessful status code
    except requests.RequestException as e:
        raise SystemExit(f"Failed to make the request. Error: {e}")

    # Handle the response as needed (e.g., print or process)
    print(response.json())


def geocode(address):
    geocode_result = gmaps.geocode(address)
    return geocode_result[0]["geometry"]["location"]


def check():
    s = "```json {\"origin\": \"South Wind Motel\", \"destination\": \"Brassica in Bexley\", \"mode\": \"walking\", \"waypoints\": \"Parsons Ave and E Main St.\", \"alternatives\": false }```"
    start_index = s.find('{')
    end_index = s.rfind('}')
    json_string = s[start_index:end_index + 1]
    print(json_string)


if __name__ == "__main__":
    # check()
    gpt()
    # origin = geocode("South Wind Motel")
    # destination = geocode("Barssica in Bexley")
    # all_routes = gmaps.directions(origin=origin, destination=destination, mode="walking", waypoints= "Parsons Ave and EMain St.", alternatives=False)
    # extract_information = {}
    # extract_information["number of route"] = len(all_routes)
    # counter = 0
    # for route in all_routes:
    #     counter = counter + 1
    #     extract_information[f"route_number_{counter}"] = route
    # print(extract_information)
    #
    # with open('my_dict.json', 'w') as json_file:
    #     json.dump(extract_information, json_file, indent=4)
    # # Printing the result
    # print(my_dist)

"""
start: 919 S High St, Columbus, OH 43206, USA
end : 

Describe a given route by providing information about the start and end locations, duration, distance, and steps without mentioning the data type. Clearly mention all the steps.

The route starts at 919 S High St in Columbus and ends at 2212 E Main St in Bexley. The total distance covered is 4 miles and the estimated time to complete the journey is 90 minutes. The route is divided into two legs. The first leg covers a distance of 1.8 miles and takes approximately 40 minutes to complete. There are three steps to follow during this leg. The first step involves heading north on S High St, the second step involves turning right onto E Whittier St, and the third step involves turning left onto Parsons Ave. The second leg covers a distance of 2.2 miles and takes approximately 50 minutes to complete. There are two steps to follow during this leg. The first step involves heading east on E Main St towards Allen Ave and the second step involves turning left onto College Ave. Thank you for following this route.
"""

"""
1: 
"context" : "Information of South Wind Motel:
                - Location: 919 S High St, Columbus, OH 43206, USA.
                Information of Brassica in Bexley:
                - Location: 2212 E Main St, Bexley, OH 43209, USA.
                There are 3 routes from South Wind Motel to Brassica in Bexley on foot. They are:
                1. Via E Main St | 1 hour 30 mins | 4.0 mi
                - Head north on S High St toward Shumacher Alley
                - Turn right onto E Whittier St
                - Turn left onto Ann St
                - Continue onto Children's Gtwy
                - At the traffic circle, take the 1st exit onto Children's Dr
                - Turn left
                - Turn right
                - Turn left toward S 18th St
                - Turn right toward S 18th St
                - Turn left onto S 18th St
                - Turn right onto E Main St
                Pass by Dollar General (on the right in 0.7 mi)
                - Turn left onto College Ave
                Destination will be on the right
                2. Via Parsons Ave and E Main St | 1 hour 30 mins | 4.0 mi
                - Head north on S High St toward Shumacher Alley
                - Turn right onto E Whittier St
                - Turn left onto Parsons Ave
                Pass by Family Dollar (on the left in 0.1 mi)
                - Turn right onto E Main St
                Pass by Dollar General (on the right in 1.1 mi)
                - Turn left onto College Ave
                Destination will be on the right
                3. Via E Whittier St and E Main St | 1 hour 30 mins | 4.0 mi
                - Head north on S High St toward Shumacher Alley
                - Turn right onto E Whittier St
                - Turn left onto S Ohio Ave
                - Turn right onto E Main St
                Pass by Dollar General (on the right in 0.5 mi)
                - Turn left onto College Ave
                Destination will be on the right
                There are 3 routes from South Wind Motel to Brassica in Bexley by car. They are:
                1. Via I-70 E | 11 mins | 4.8 mi
                2. Via E Whittier St | 12 mins | 4.1 mi
                3. Via E Main St | 13 mins | 4.0 mi
                There are 3 routes from South Wind Motel to Brassica in Bexley by cycle. They are:
                1. Via E Main St | 23 mins | 4.0 mi
                2. Via E Whittier St and E Main St | 23 mins | 4.0 mi
                3. Via E Whittier St | 23 mins | 4.0 mi
                There are 6 routes from South Wind Motel to Brassica in Bexley by public transport. They are:
                1. Via | 38 mins | 4.1 mi
                2. Via | 25 mins | 4.1 mi
                3. Via | 34 mins | 4.5 mi
                4. Via | 44 mins | 4.5 mi
                5. Via | 26 mins | 4.1 mi
                6. Via | 41 mins | 4.1 mi",
"""
"""
2:
"context" : "Context (Template)
    Information of Mittelpunkt Deutschlands:

    - Location: An d. Oberrothe, 99986 Vogtei, Germany.

    Information of Wildkatzendorf Hütscheroda:

    - Location: Schloßstraße 4, 99820 Hörselberg-Hainich, Germany.

    Information of D03 Flame Tree Ridge:

    - Location: 2674+M59 D32 Flame Tree Ridge - D03 - Jumeirah Golf Estates - Dubai - United Arab Emirates.

    Information of Aster Cedars Hospital, Jebel Ali:

    - Location: Street No.2 - Mina Jebel Ali - Jebel Ali Freezone - Dubai - United Arab Emirates.

    There are 2 routes from D03 Flame Tree Ridge to Aster Cedars Hospital, Jebel Ali by car. They are:

    1. Via D57 | 18 mins | 17.9 km

    - Head southwest
    Restricted usage road

    - At the roundabout, take the 2nd exit

    - At the roundabout, take the 1st exit
    Go through 1 roundabout

    - Turn left onto Al Fay Rd

    - At the roundabout, take the 2nd exit

    - Continue onto Al Fay Rd

    - Take the ramp to Al Khail Rd/E44

    - Take the ramp to Al Khail Rd/E44

    - Continue onto Al Khail Rd/E44

    - Take the E311 S/Sh Mohammed Bin Zayed Rd exit toward DWC Airport/Abu Dhabi

    - Take the ramp onto Sheikh Mohammed Bin Zayed Rd/E311

    - Take exit 22 for Al Yalayis St/D57 W toward PJA Port

    - Take the ramp onto D57

    - Take the ramp

    - Take the ramp

    - Take the ramp

    - Take the exit

    - Slight left toward 511 Street‎

    - Continue onto 511 Street‎
    Destination will be on the right

    2. Via Garn Al Sabkha St/D59 | 26 mins | 24.1 km

    - Head southwest
    Restricted usage road

    - At the roundabout, take the 2nd exit

    - At the roundabout, take the 1st exit
    Go through 1 roundabout

    - Turn left onto Al Fay Rd

    - At the roundabout, take the 2nd exit

    - Continue onto Al Fay Rd

    - Take the ramp to Al Khail Rd/E44

    - Take the ramp to Al Khail Rd/E44

    - Continue onto Al Khail Rd/E44

    - Take the E311 S/Sh Mohammed Bin Zayed Rd exit toward DWC Airport/Abu Dhabi

    - Slight right onto the ramp to Garn Al Sabkha St/D59

    - Take the ramp to Garn Al Sabkha St/D59

    - Keep right at the fork to continue toward Garn Al Sabkha St/D59

    - Continue onto Garn Al Sabkha St/D59

    - Keep left to stay on Garn Al Sabkha St/D59

    - Merge onto Sheikh Zayed Rd/E11 via the ramp to Jebel Ali/Abu Dhabi

    - Continue straight to stay on Sheikh Zayed Rd/E11
    Toll road

    - Take exit 22 toward PJA Port Gate 1/PJA Port Gate 2

    - Keep right

    - Turn right onto 511 Street‎
    Destination will be on the right

    There are 3 routes from D03 Flame Tree Ridge to Aster Cedars Hospital, Jebel Ali on foot. They are:

    1. Via Sheikh Zayed Bin Hamdan Al Nahyan Street/D54 | 7 hours 11 mins | 31.7 km

    2. Via Al Asayel St/D72 | 9 hours 41 mins | 42.4 km

    3. Via Hessa St/D61 | 9 hours 44 mins | 42.2 km

    Current location of user is D03 Flame Tree Ridge.

    Context (GPT)
    The Mittelpunkt Deutschlands is located at An d. Oberrothe, 99986 Vogtei, Germany. The Wildkatzendorf Hütscheroda is situated at Schloßstraße 4, 99820 Hörselberg-Hainich, Germany. D03 Flame Tree Ridge is located at 2674+M59 D32 Flame Tree Ridge - D03 - Jumeirah Golf Estates, Dubai, United Arab Emirates. Aster Cedars Hospital in Jebel Ali is located at Street No.2, Mina Jebel Ali, Jebel Ali Freezone, Dubai, United Arab Emirates.

    There are two car routes from D03 Flame Tree Ridge to Aster Cedars Hospital in Jebel Ali:
    1. Via D57: This route takes about 18 minutes covering a distance of 17.9 km.
    2. Via Garn Al Sabkha St/D59: This route takes approximately 26 minutes covering a distance of 24.1 km.

    There are three walking routes from D03 Flame Tree Ridge to Aster Cedars Hospital in Jebel Ali:
    1. Via Sheikh Zayed Bin Hamdan Al Nahyan Street/D54: This route takes about 7 hours and 11 minutes covering a distance of 31.7 km.
    2. Via Al Asayel St/D72: This route takes approximately 9 hours and 41 minutes covering a distance of 42.4 km.
    3. Via Hessa St/D61: This route takes about 9 hours and 44 minutes covering a distance of 42.2 km.

    The current location of the user is D03 Flame Tree Ridge.",
"""



