import tweepy
from stream_listener import MyStreamListener
from api import api
from secret import handle

# string array of words that will trigger the on_status function
trigger_words = [
    '@' + handle # respond to @mentions
]

print('Bot online -------------\n')
streamListener = MyStreamListener()
stream = tweepy.Stream(auth = api.auth, listener=streamListener)
stream.filter(track=trigger_words)