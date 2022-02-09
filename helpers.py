import requests

API = 'https://api.hatchways.io/assessment/blog/posts'

def ping_api_response(tag):
    """Returns api call response"""
    payload = {'tag': tag}
    res = requests.get(API, params=payload)
    return res

#### TODO ####
# def get_tags_from_url(url)