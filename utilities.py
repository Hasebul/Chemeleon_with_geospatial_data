import time
import random
import requests
import os
import openai
import json
import base64
import googlemaps
import func_timeout
import requests
import numpy as np

from typing import Union, Any
from math import isclose
from openai import AzureOpenAI
from math import sin, cos, sqrt, atan2, radians

gmaps = googlemaps.Client(key='AIzaSyBnsinvIK8T2C8Kv5Q3gKyVWaTMgINDhVw')


def safe_execute(code_string: str, keys=None):
    def execute(x):
        try:
            exec(x)
            locals_ = locals()
            if keys is None:
                return locals_.get('ans', None)
            else:
                return [locals_.get(k, None) for k in keys]
        except Exception:
            return None

    try:
        ans = func_timeout.func_timeout(1, execute, args=(code_string,))
    except func_timeout.FunctionTimedOut:
        ans = None
    return ans


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


def place(query, location, region, type):
    places_results = gmaps.places(
        query=query,
        location=location,
        # region=region,
        type=type
    )
    all_poi = places_results["results"]
    extract_information = f"The following location are the nearest location and all the location has a destination form the current location {location}:\n"
    for poi in all_poi:
        dist = distance(loc1=poi['geometry']['location'], loc2=location)
        rating = poi['rating'] if 'rating' in poi.keys() else 0
        total_user = poi['user_ratings_total'] if 'user_ratings_total' in poi.keys() else 0
        extract_information = extract_information + f"{poi['name']} has {rating} rating," + f"where {total_user} people give their rating, " + f"the location distance from current location is {dist} kilometers\n"
    return extract_information


def geocode(address):
    geocode_result = gmaps.geocode(address)
    return geocode_result[0]["geometry"]["location"]


def directions(origin, destination, mode=None, waypoints=None, alternatives=True):
    # origin = "D03 Flame Tree Ridge", destination = "Aster Cedars Hospital, Jebel Ali", mode = "driving", waypoints = None, alternatives = True
    all_routes = gmaps.directions(
        origin=origin, destination=destination, mode=mode, waypoints=waypoints, alternatives=alternatives
    )

    extract_information = {}
    extract_information["number of route"] = len(all_routes)
    counter = 0
    for route in all_routes:
        counter = counter + 1
        extract_information[f"route_number_{counter}"] = route
    print(extract_information)
    return extract_information


def get_codex_response(prompt, api_key, engine="code-davinci-002", temperature=0, max_tokens=256, top_p=1, n=1,
                       patience=10, sleep_time=0):
    while patience > 0:
        patience -= 1
        try:
            response = openai.Completion.create(engine=engine,
                                                prompt=prompt,
                                                api_key=api_key,
                                                temperature=temperature,
                                                max_tokens=max_tokens,
                                                top_p=top_p,
                                                n=n,
                                                stop=['\n\n'],
                                                frequency_penalty=0,
                                                presence_penalty=0)
            prediction = response["choices"][0]["text"].strip()
            if prediction != "" and prediction != None:
                return prediction
        except Exception as e:
            print(e)
            if sleep_time > 0:
                time.sleep(sleep_time)
    return ""


def get_gpt3_response(prompt, api_key, engine="text-davinci-002", temperature=0, max_tokens=256, top_p=1, n=1,
                      patience=100, sleep_time=0):
    while patience > 0:
        patience -= 1
        try:
            response = openai.Completion.create(engine=engine,
                                                prompt=prompt,
                                                api_key=api_key,
                                                temperature=temperature,
                                                max_tokens=max_tokens,
                                                top_p=top_p,
                                                n=n,
                                                stop=['\n\n'],
                                                frequency_penalty=0,
                                                presence_penalty=0)
            prediction = response["choices"][0]["text"].strip()
            if prediction != "" and prediction != None:
                return prediction
        except Exception as e:
            print(e)
            if sleep_time > 0:
                time.sleep(sleep_time)
    return ""


# def get_chat_response(messages, api_key, model="gpt-3.5-turbo", temperature=0, max_tokens=256, n=1, patience=100, sleep_time=0):
#     while patience > 0:
#         patience -= 1
#         try:
#             response = openai.ChatCompletion.create(model=model,
#                                                 messages=messages,
#                                                 api_key=api_key,
#                                                 temperature=temperature,
#                                                 max_tokens=max_tokens,
#                                                 n=n)
#             if n == 1:
#                 prediction = response['choices'][0]['message']['content'].strip()
#                 if prediction != "" and prediction != None:
#                     return prediction
#             else:
#                 prediction = [choice['message']['content'].strip() for choice in response['choices']]
#                 if prediction[0] != "" and prediction[0] != None:
#                     return prediction
#
#         except Exception as e:
#             print(e)
#             if sleep_time > 0:
#                 time.sleep(sleep_time)
#     return ""


def get_chat_response(messages, api_key, model="gpt-3.5-turbo", temperature=0, max_tokens=256, n=1, patience=100,
                      sleep_time=0):
    while patience > 0:
        patience -= 1
        try:
            # their gpt
            # response = openai.ChatCompletion.create(model=model,
            #                                     messages=messages,
            #                                     api_key=api_key,
            #                                     temperature=temperature,
            #                                     max_tokens=max_tokens,
            #                                     n=n)
            # if n == 1:
            #     prediction = response['choices'][0]['message']['content'].strip()
            #     if prediction != "" and prediction != None:
            #         return prediction
            # else:
            #     prediction = [choice['message']['content'].strip() for choice in response['choices']]
            #     if prediction[0] != "" and prediction[0] != None:
            #         return prediction
            # Azure
            client = AzureOpenAI(
                azure_endpoint="https://llms-eus2.openai.azure.com/",
                api_key="c7d579ff57394bf98d6da39f9c96bca5",
                api_version="2024-05-01-preview",
            )
            response = client.chat.completions.create(
                model="gpt-35-turbo-0125",
                messages=messages,
                temperature=temperature,
                max_tokens=max_tokens,
                top_p=0.95,
                frequency_penalty=0,
                presence_penalty=0,
                stop=None,
                n=n
            )
            if n == 1:
                prediction = response.choices[0].message.content.strip()
                if prediction != "" and prediction != None:
                    return prediction
            else:
                prediction = [choice.message.content.strip() for choice in response.choices]
                if prediction[0] != "" and prediction[0] != None:
                    return prediction

        except Exception as e:
            print(e)
            if sleep_time > 0:
                time.sleep(sleep_time)
    return ""


# def get_chat_response(messages, api_key, model="gpt-3.5-turbo", temperature=0, max_tokens=256, n=1, patience=100,
#                       sleep_time=0):  # gpt4
#     while patience > 0:
#
#         patience -= 1
#         try:
#
#             # Configuration
#             API_KEY = "01488083a8d243e684bd48a39152d90a"
#             # API_KEY = "YOUR_API_KEY"
#             # IMAGE_PATH = "YOUR_IMAGE_PATH"
#             # encoded_image = base64.b64encode(open(IMAGE_PATH, 'rb').read()).decode('ascii')
#             headers = {
#                 "Content-Type": "application/json",
#                 "api-key": API_KEY,
#             }
#
#             # Payload for the request
#             payload = {
#                 "messages": messages,
#                 "temperature": 0.7,
#                 "top_p": 0.95,
#                 "max_tokens": 1000
#             }
#             # GPT-35-TURBO-0125
#             ENDPOINT = "https://qcri-llm-rag-4.openai.azure.com/openai/deployments/GPT-4o/chat/completions?api-version=2024-02-15-preview"
#
#             # Send request
#             try:
#                 response = requests.post(ENDPOINT, headers=headers, json=payload)
#                 response.raise_for_status()  # Will raise an HTTPError if the HTTP request returned an unsuccessful status code
#             except requests.RequestException as e:
#                 raise SystemExit(f"Failed to make the request. Error: {e}")
#             if n == 1:
#                 rep = response.json()
#                 prediction = rep["choices"][0]["message"]["content"].strip()
#                 # print(prediction)
#                 if prediction != "" and prediction != None:
#                     return prediction
#             else:
#                 prediction = [choice.message.content.strip() for choice in response.choices]
#                 if prediction[0] != "" and prediction[0] != None:
#                     return prediction
#
#         except Exception as e:
#             print(e)
#             if sleep_time > 0:
#                 time.sleep(sleep_time)
#     return ""


# def get_chat_response(messages, api_key, model="gpt-3.5-turbo", temperature=0, max_tokens=256, n=1, patience=100,
#                       sleep_time=0):  # gpt4
#     while patience > 0:
#
#         patience -= 1
#         try:
#
#
#             # Configuration
#             API_KEY = "154bfc83018f41f19341d76cefe5d95c"
#             # API_KEY = "YOUR_API_KEY"
#             # IMAGE_PATH = "YOUR_IMAGE_PATH"
#             # encoded_image = base64.b64encode(open(IMAGE_PATH, 'rb').read()).decode('ascii')
#             headers = {
#                 "Content-Type": "application/json",
#                 "api-key": API_KEY,
#             }
#
#             # Payload for the request
#             payload = {
#                 "messages": messages,
#                 "temperature": 0.7,
#                 "top_p": 0.95,
#                 "max_tokens": 1000
#             }
#             # GPT-35-TURBO-0125
#             ENDPOINT = "https://qcri-llm-rag-3.openai.azure.com/openai/deployments/gpt-35-turbo/chat/completions?api-version=2023-03-15-preview"
#
#             # Send request
#             try:
#                 response = requests.post(ENDPOINT, headers=headers, json=payload)
#                 response.raise_for_status()  # Will raise an HTTPError if the HTTP request returned an unsuccessful status code
#             except requests.RequestException as e:
#                 raise SystemExit(f"Failed to make the request. Error: {e}")
#             if n == 1:
#                 rep = response.json()
#                 prediction = rep["choices"][0]["message"]["content"].strip()
#                 # print(prediction)
#                 if prediction != "" and prediction != None:
#                     return prediction
#             else:
#                 prediction = [choice.message.content.strip() for choice in response.choices]
#                 if prediction[0] != "" and prediction[0] != None:
#                     return prediction
#
#         except Exception as e:
#             print(e)
#             if sleep_time > 0:
#                 time.sleep(sleep_time)
#     return ""


def floatify_ans(ans):
    if ans is None:
        return None
    elif type(ans) == dict:
        ans = list(ans.values())[0]
    elif type(ans) == bool:
        ans = ans
    elif type(ans) in [list, tuple]:
        if not ans:
            return None
        else:
            try:
                ans = float(ans[0])
            except Exception:
                ans = str(ans[0])
    else:
        try:
            ans = float(ans)
        except Exception:
            ans = str(ans)
    return ans


def score_string_similarity(str1, str2):
    if str1 == str2:
        return 2.0
    elif " " in str1 or " " in str2:
        str1_split = str1.split(" ")
        str2_split = str2.split(" ")
        overlap = list(set(str1_split) & set(str2_split))
        return len(overlap) / max(len(str1_split), len(str2_split))
    else:
        return 0.0


def normalize_prediction_tabmwp(prediction, options=None, unit=None):
    # the numerical answer
    if isinstance(prediction, float):
        prediction = round(prediction, 3)
        return prediction

    # the string answer
    if isinstance(prediction, str):
        prediction = prediction.replace('$', '')
        if unit:
            prediction = prediction.replace(unit, '')
        prediction = prediction.strip().lower()

        if not options:
            # numeric answer: convert to float
            try:
                if '/' in prediction:
                    prediction = int(prediction.split('/')[0]) / int(prediction.split('/')[1])
                elif ',' in prediction:
                    prediction = float(prediction.replace(',', ''))
                elif '%' in prediction:
                    prediction = float(prediction.split('%')[0]) / 100
                else:
                    prediction = float(prediction)
            except Exception:
                pass

                # the string answer from choices
    if options:
        options = [x.lower() for x in options]
        if prediction is None:
            prediction = options[0]
        elif isinstance(prediction, str):
            if prediction not in options:
                # find the most similar option
                scores = [score_string_similarity(x, prediction) for x in options]
                max_idx = int(np.argmax(scores))  # json does not recognize NumPy data types
                prediction = options[max_idx]
    return prediction


def normalize_ground_tabmwp(gt_ans, ans_type=None):
    if ans_type in ['integer_number', 'decimal_number']:
        if '/' in gt_ans:
            gt_ans = int(gt_ans.split('/')[0]) / int(gt_ans.split('/')[1])
        elif ',' in gt_ans:
            gt_ans = float(gt_ans.replace(',', ''))
        elif '%' in gt_ans:
            gt_ans = float(gt_ans.split('%')[0]) / 100
        else:
            gt_ans = float(gt_ans)
    elif ans_type.endswith('_text'):
        gt_ans = str(gt_ans)
    else:
        raise ValueError(ans_type)
    return gt_ans


def normalize_ground_scienceqa(gt_ans):
    gt_ans = gt_ans.lower()
    return gt_ans


def normalize_prediction_scienceqa(prediction, options=None):
    # the string answer from choices
    if options:
        options = [x.lower() for x in options]
        if prediction is None:
            prediction = options[0]
        elif isinstance(prediction, str):
            if prediction not in options:
                # find the most similar option
                scores = [score_string_similarity(x, prediction) for x in options]
                max_idx = int(np.argmax(scores))  # json does not recognize NumPy data types
                prediction = options[max_idx]
    return prediction


def get_precision(gt_ans: float) -> int:
    precision = 5
    if '.' in str(gt_ans):
        precision = len(str(gt_ans).split('.')[-1])
    return precision


def safe_equal(prediction: Union[bool, float, str],
               reference: Union[float, str],
               include_percentage: bool = False,
               is_close: float = False) -> bool:
    if prediction is None:
        return False
    elif type(prediction) == bool:
        # bool questions
        if prediction:
            return reference == 'yes'
        else:
            return reference == 'no'
    elif type(reference) == str and type(prediction) == str:
        # string questions
        prediction = prediction.strip().lower()
        reference = reference.strip().lower()
        return prediction == reference
    else:
        # number questions
        if include_percentage:
            gt_result = [reference / 100, reference, reference * 100]
        else:
            gt_result = [reference]
        for item in gt_result:
            try:
                if is_close:
                    if isclose(item, prediction, rel_tol=0.001):
                        return True
                precision = min(get_precision(prediction), get_precision(item))
                if round(prediction, precision) == round(item, precision):
                    return True
            except Exception:
                continue
        return False


def _validate_server(address):
    if not address:
        raise ValueError('Must provide a valid server for search')
    if address.startswith('http://') or address.startswith('https://'):
        return address
    PROTOCOL = 'http://'
    print(f'No protocol provided, using "{PROTOCOL}"')
    return f'{PROTOCOL}{address}'


def call_bing_search(endpoint, bing_api_key, query, count):
    headers = {'Ocp-Apim-Subscription-Key': bing_api_key}
    params = {"q": query, "textDecorations": True,
              "textFormat": "HTML", "count": count, "mkt": "en-GB"}
    try:
        server = _validate_server(endpoint)  # server address
        server_response = requests.get(server, headers=headers, params=params)
        resp_status = server_response.status_code
        if resp_status == 200:
            result = server_response.json()
            return result
    except:
        pass

    return None


def parse_bing_result(result):
    responses = []
    try:
        value = result["webPages"]["value"]
    except:
        return responses

    for i in range(len(value)):
        snippet = value[i]['snippet'] if 'snippet' in value[i] else ""
        snippet = snippet.replace("<b>", "").replace("</b>", "").strip()
        if snippet != "":
            responses.append(snippet)

    return responses
