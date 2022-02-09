import requests

API = 'https://api.hatchways.io/assessment/blog/posts'

def ping_api_response():
    """Returns api call response"""
    payload = {'tag': 'all'}
    res = requests.get(API, params=payload)
    return res