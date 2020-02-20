import tweepy
from secret import consumer_key, consumer_secret, access_token, access_secret

# get authentication info
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

# log into the API
api = tweepy.API(auth)