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

# print api.get_user('softwarestudies')
# print api.get_status(868579630294413312)

# print api.home_timeline(count=5)
print api.get_status(855143102876536832)
# api.retweet(876953479302057984)
# print api.user_timeline()[12]._json

# print api.geo_id('1d9a5370a355ab0c')


# user(class) vs user._json(json) result: identical(43(evl_uic);44(softwarestudies))
# user.status(class) vs user.status._json(json) vs user._json.status(json) result: different(26:25:25)
# user.status.retweeted_status(class) vs
#   user.status.retweeted_status._json(json) vs
#   user.status._json.retweeted_status(json) vs
#   user._json.status.retweeted_status(json) (25:24:24:24)

## compares class and its json for the same thing
# status(class) vs status._json(json) result: different(30:28)
# status.user(class) vs
#   status.user._json(json) vs
#   status._json.user(json) result: identical(41(evl_uic);42(softwarestudies))

## compares json
# status.quoted_status(json) vs status._json.quoted_status(json) result: identical(25)
# status.quoted_status.user(json) vs status._json.quoted_status.user result: identical(42)

# 41: - profile_location; - banner_url; - status (@evl_uic from Status)
# 42: + profile_location; - banner_url; - status (@softwarestudies from Status.quoted_status)
# 43: + profile_location; - banner_url; + status (@evl_uic from User)
# 44: + profile_location; + banner_url; + status (@softwarestudies from User)
# 42(json) (@softwarestudies from Status)