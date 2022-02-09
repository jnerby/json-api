import requests

API = 'https://api.hatchways.io/assessment/blog/posts'

def get_tag_responses(tags: list) -> list:
    tag_responses = []    
    # call api for each tag and push to a set - SET COMP NOT WORKING
    for tag in tags:
        res = ping_api_response(tag).json()
        tag_responses.extend(res['posts'])

    return remove_duplicate_posts(tag_responses)

## TYPE INDICATOR FOR RESPONSE?
def ping_api_response(tag: str):
    """Returns api call response"""
    payload = {'tag': tag}
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
        if response['id'] not in api_calls_ids:
            result.append(response)            
            api_calls_ids.add(response['id'])

    return result

def sort_result(result: list, sort_by_value: str, sort_direction: str) -> list:
    """Sorts responses"""
    if sort_direction == 'desc':
        sorted_result = sorted(result, key=lambda i: i[sort_by_value], reverse=True)
    else:
        sorted_result = sorted(result, key=lambda i: i[sort_by_value])
    return sorted_result

#### TODO ####
# def get_tags_from_url(url)