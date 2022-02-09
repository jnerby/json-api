import helpers
import json
from flask import Flask, jsonify, redirect

app = Flask(__name__)

@app.route('/')
def reroute_home():
    return redirect('/api/posts')

@app.route('/api/ping')
def ping_api():
    """Returns status code from pinging API"""
    # get response from pinging API
    res = helpers.ping_api_response('all')
    if res.status_code == 200:
        return jsonify({"success": "true"})
    return jsonify({"success": "false"})

@app.route('/api/posts')
def return_api_posts():
    """Returns all posts with at least one tag specified"""
    #### WHERE DOES URL COME FROM _ HOW TO SPLIT TAGS???
    # get list of tags user passed in
    tags = ['tech', 'history', 'health']

    # empty list for all tag calls including dupes
    tag_calls = []
    
    # init set for unique post ids
    api_calls_ids = set()
    # empty list for unique results
    result = []

    # call api for each tag and push to a set - SET COMP NOT WORKING
    for tag in tags:
        res = helpers.ping_api_response(tag).json()
        tag_calls.extend(res['posts'])

    # remove duplicate calls
    for call in tag_calls:
        if call['id'] not in api_calls_ids:
            result.append(call)            
            api_calls_ids.add(call['id'])

    # sort results
    ### HOW TO EXTRACT SORT PREFERENCES
    sort_by_value = 'likes'
    sort_direction = 'desc'
    if not sort_direction:
        return jsonify(result)
    
    if sort_direction == 'desc':
        sorted_result = sorted(result, key=lambda i: i[sort_by_value], reverse=True)
    else:
        sorted_result = sorted(result, key=lambda i: i[sort_by_value])

    return jsonify(sorted_result)

if __name__ == '__main__':
    app.run(debug=True)