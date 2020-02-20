import praw
from reddit import reddit
import time

## REMOVE THESE TWO LINES ##
import sys
sys.path.append('../..')

from BasicBot import respond

if __name__ == '__main__':

    print('Bot running ------------\n')
    
    while True:

        # check unread messages in the inbox
        for message in reddit.inbox.unread(limit=None):

            # mark the message as read so it doesn't get processed again
            message.mark_read()

            # only look at mentions
            subject = message.subject.lower()
            if isinstance(message, praw.models.Comment) and subject == 'username mention':

                print('Got a message: {}'.format(message.body))

                # respond to the message
                content = message.body.split(' ', 1)[1]
                message.reply(respond(content))

        # wait 5s to check again
        time.sleep(5)