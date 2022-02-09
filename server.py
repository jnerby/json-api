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
    res = helpers.call_api('all')
    if res.status_code == 200:
        return jsonify({"success": "true"})
    return jsonify({"success": "false"})

@app.route('/api/posts/<tags>')
def return_api_posts(tags):
    """Returns all posts with at least one tag specified"""
    #### WHERE DOES URL COME FROM _ HOW TO SPLIT TAGS???
    # get list of tags user passed in
    print(tags)
    # tag_list = [tags]
    tag_list = tags.split(',')
    # tags = ['tech', 'history', 'health']
    
    # get unique responses
    result = helpers.get_tag_responses(tag_list)
    print(len(result))

    ### HOW TO EXTRACT SORT PREFERENCES
    sort_by_value = 'popularity'
    sort_direction = None

    # return result if no sort direction specified
    if not sort_direction:
        return jsonify(result)
    
    # return sorted responses
    return jsonify(helpers.sort_result(result, sort_by_value, sort_direction))

if __name__ == '__main__':
    app.run(debug=True)