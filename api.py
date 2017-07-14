#!/usr/bin/env python

#Import the necessary methods from tweepy library
# from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
# from tweepy import Stream
from tweepy import API

#Variables that containthe user credentials to access Twitter API
access_token = "104091062-HpVVxBLednHslOI5EvrIEAzgJPq21Kde4hBAMk6k"
access_token_secret = "g9sZgWMKheVVw5QuiJSvaPhMnMUDLa7ZSDuII225JF9wu"
consumer_key = "lstgqdhAx3sMAERAs2z37DWX5"
consumer_secret = "BkklxVh7jwvRYGerChWpOHEGrc4EjlWalgKu88J5feNx0TPVVa"

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = API(auth)

# user = api.get_user('joyswordy')
# print api.home_timeline(count=5)
print api.get_status(849201805569343488)._json
# api.retweet(876953479302057984)
# print api.user_timeline()[12]._json

# print api.geo_id('1d9a5370a355ab0c')
