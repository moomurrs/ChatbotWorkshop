import tweepy
from api import api

## REMOVE THESE TWO LINES ##
import sys
sys.path.append('../..')

from BasicBot import respond

# override the default listener to add code to on_status
class MyStreamListener(tweepy.StreamListener):

    # listener for tweets
    # -------------------
    # this function will be called any time a tweet comes in
    # that contains words from the array created above
    def on_status(self, status):

        # log the incoming tweet
        print('Received: "{}" from @{}'.format(
            status.text,
            status.author.screen_name
        ))

        # process content
        content = status.text.split(" ", 1)[1]
        reply = respond(content)

        # respond to the tweet
        api.update_status(
            status="@{} {}".format(status.author.screen_name, reply),
            in_reply_to_status_id=status.id
        )