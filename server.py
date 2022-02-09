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
    
    # get unique 
    result = helpers.get_tag_responses(tags)

    ### HOW TO EXTRACT SORT PREFERENCES
    sort_by_value = 'popularity'
    sort_direction = 'desc'

    if not sort_direction:
        return jsonify(result)
    
    return jsonify(helpers.sort_result(result, sort_by_value, sort_direction))

if __name__ == '__main__':
    app.run(debug=True)