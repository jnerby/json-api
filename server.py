import helpers
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/ping')
def render_home():
    res = helpers.ping_api_response()
    print(res)
    if res.status_code == 200:
        return jsonify({"success": "true"})
    return helpers.ping_api_response().json()

if __name__ == '__main__':
    app.run(debug=True)