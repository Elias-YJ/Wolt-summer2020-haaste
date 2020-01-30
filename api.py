import flask
import json
from flask import request, jsonify
from helper_functions import none_handler

app = flask.Flask(__name__)
app.config["DEBUG"] = True
app.config["JSON_AS_ASCII"] = False

with open('restaurants.json') as json_file:
    restaurant_data = json.loads(json_file.read())


@app.route('/', methods=['GET'])
def home():
    return '''<h1>Wolt Restaurant API</h1>
<p>Summer 2020 Challenge API for searching restaurants.</p>'''


# A route to return all of the available entries in our catalog.
@app.route('/restaurants', methods=['GET'])
def api_all():
    return jsonify(restaurant_data)


# A route to search for a restaurant nearby.
@app.route('/restaurants/search', methods=['GET'])
def api_id():
    # Check if search is valid
    if 'q' in request.args:
        q = str(request.args['q'])
    else:
        return "Error: No query argument provided. Please specify a query keyword."

    # Return restaurants that have a match by filtering others.
    results = list(filter(lambda x: q.lower() in none_handler(x['description']).lower()
                          or q.lower() in none_handler(x['name']).lower()
                          or next((tag for tag in x['tags']
                                   if q.lower() in none_handler(tag).lower()), None) is not None
                          , restaurant_data['restaurants']))
    results = {'restaurants': results}

    return jsonify(results)


if __name__ == '__main__':
    app.run()
