import requests
from flask import jsonify

API = "https://api.hatchways.io/assessment/blog/posts"


def get_tag_responses(tags: list) -> list:
    tag_responses = []
    # call api for each tag and push to a set - SET COMP NOT WORKING
    for tag in tags:
        res = call_api(tag).json()
        tag_responses.extend(res["posts"])

    return remove_duplicate_posts(tag_responses)


def call_api(tag: str) -> object:
    """Returns api call response"""
    payload = {"tag": tag}
    res = requests.get(API, params=payload)
    return res


def remove_duplicate_posts(tag_responses: list) -> list:
    """Removes duplicate posts in tag_responses list"""
    # init set for unique post ids
    api_calls_ids = set()
    # empty list for unique results
    result = []

    # remove duplicate calls
    for response in tag_responses:
        if response["id"] not in api_calls_ids:
            result.append(response)
            api_calls_ids.add(response["id"])

    return result


def sort_result(result: list, sort_by_value: str, sort_direction: str) -> list:
    """Sorts responses"""
    # get all keys
    keys = set(result[0].keys())

    # check that sort_by_value is valid key
    if sort_by_value in keys:
        if sort_direction == "desc":
            sorted_result = sorted(result, key=lambda i: i[sort_by_value], reverse=True)
        elif sort_direction == "asc":
            sorted_result = sorted(result, key=lambda i: i[sort_by_value])

        return sorted_result

    # if sort_by_value or sort_direction invalid, return erro
    return {"error": "sortBy parameter is invalid"}, 400
