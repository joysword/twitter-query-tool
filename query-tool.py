import json
import os.path

from flask import Flask, render_template, request, jsonify
from tweepy import OAuthHandler
from tweepy import API

from utils import exist, get_file

#Variables that containthe user credentials to access Twitter API
access_token = "104091062-HpVVxBLednHslOI5EvrIEAzgJPq21Kde4hBAMk6k"
access_token_secret = "g9sZgWMKheVVw5QuiJSvaPhMnMUDLa7ZSDuII225JF9wu"
consumer_key = "lstgqdhAx3sMAERAs2z37DWX5"
consumer_secret = "BkklxVh7jwvRYGerChWpOHEGrc4EjlWalgKu88J5feNx0TPVVa"

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = API(auth)

app = Flask(__name__)


# @app.route('/', methods=['GET', 'POST'])
# def index():
#     if request.method == 'POST':
#         return 'haha'
#     else:
#         return render_template('index.html')

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/get/place')
def get_place():
    place_id = request.args.get('id')

    if not exist('place', place_id):
        place = api.geo_id(place_id)

        feature = {
            'type': 'Feature',
            'properties': {
                'type': place.place_type,
                'id': place.id,
                'name': place.name,
                'full name': place.full_name,
                'centroid (lon, lat)': place.centroid,
                'country code': place.country_code,
                'contained id': place.contained_within[0].id,
                'contained name': place.contained_within[0].name,
                'contained full name': place.contained_within[0].full_name,
                'contained type': place.contained_within[0].place_type,
            },
            'geometry': {
                'type': place.bounding_box.type,
                'coordinates': place.bounding_box.coordinates
            }
        }
        with open(os.path.join('static', 'json', 'place', place_id+'.json'), 'w') as json_file:
            json.dump(feature, json_file)
        return jsonify(feature)
    else:
        with open(get_file('place', place_id), 'r') as json_data:
            ret = json.load(json_data)
        return jsonify(ret)


@app.route('/get/user')
def get_user():
    user_id = request.args.get('id')

    if not exist('user', user_id):
        user = api.get_status(user_id)

        feature = {
            'type': 'Feature',
            'properties': {
                'id': user.id_str,
                'followers': user.followers_count,
                'tweets': user.statuses_count,
                'following': user.friends_count,
                'name (real)': user.name,
                'name (screen)': user.screen_name,
                'location': user.location,
                'most recent tweet': user.status.text,  # TODO: tweepy's Status does not have extended text
            }
        }

        has_coord = True if user.coordinates else False

        feature = {
            'type': 'Feature',
            'properties': {
                'id': user.id_str,
                'text': text,
                'precise': has_coord
            },
            'geometry': user.coordinates
        }
        with open(os.path.join('static', 'json', 'user', user_id+'.json'), 'w') as json_file:
            json.dump(feature, json_file)
        return jsonify(feature)
    else:
        with open(get_file('user', user_id), 'r') as json_data:
            ret = json.load(json_data)
        return jsonify(ret)


@app.route('/get/tweet')
def get_tweet():
    tweet_id = request.args.get('id')

    if not exist('tweet', tweet_id):
        tweet = api.get_status(tweet_id)

        # TODO: tweet.extended_tweet.full_text is probably wrong syntax
        text = tweet.text if tweet.truncated else tweet.extended_tweet.full_text

        has_coord = True if tweet.coordinates else False

        feature = {
            'type': 'Feature',
            'properties': {
                'id': tweet.id_str,
                'text': text,
                'precise': has_coord
            },
            'geometry': tweet.coordinates
        }
        with open(os.path.join('static', 'json', 'tweet', tweet_id+'.json'), 'w') as json_file:
            json.dump(feature, json_file)
        return jsonify(feature)
    else:
        with open(get_file('tweet', tweet_id), 'r') as json_data:
            ret = json.load(json_data)
        return jsonify(ret)


if __name__ == '__main__':
    app.run(debug=True)
