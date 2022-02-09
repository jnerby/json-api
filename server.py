import helpers
from flask import Flask, jsonify, redirect
from flask_caching import Cache


config = {"DEBUG": True, "CACHE_TYPE": "SimpleCache", "CACHE_DEFAULT_TIMEOUT": 300}

app = Flask(__name__)
app.config.from_mapping(config)
cache = Cache(app)


@app.route("/")
@cache.cached(timeout=2)
def reroute_home():
    print("cached")
    return redirect("/api/posts")


@app.route("/api/ping")
def ping_api():
    """Returns status code from pinging API"""
    # get response from pinging API
    res = helpers.call_api("all")
    if res.status_code == 200:
        return jsonify({"success": "true"})
    return jsonify({"success": "false"})


@app.route("/api/posts")
@app.route("/api/posts/<tags>")
@app.route("/api/posts/<tags>/<sort_by_value>")
@app.route("/api/posts/<tags>/<sort_by_value>/<sort_direction>")
@cache.cached(timeout=50)
def return_api_posts(tags=None, sort_by_value=None, sort_direction="asc"):
    """Returns all posts with at least one tag specified"""
    # error if no tags passed in
    if not tags:
        return jsonify({"error": "Tags parameter is required"}), 400

    # get list of tags user passed in
    tag_list = tags.split(",")

    # get unique responses
    result = helpers.get_tag_responses(tag_list)

    # return result if no sort direction specified
    if not sort_by_value:
        return jsonify(result)

    # return sorted responses
    return jsonify({"posts" : helpers.sort_result(result, sort_by_value, sort_direction)}), 200


if __name__ == "__main__":
    app.run(debug=True)
