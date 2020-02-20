import os
import slack
from secret import bot_token

## REMOVE THESE TWO LINES ##
import sys
sys.path.append('../..')

from BasicBot import respond

@slack.RTMClient.run_on(event='message')
def respond_to_message(**payload):

    data = payload['data']
    
    if 'subtype' in data and data['subtype'] == 'bot_message':
        return

    web_client = payload['web_client']
    content = data['text']

    print('Got a message: {}'.format(content))

    if content.startswith('<@'):
        content = content.split(' ', 1)[1]
    
    channel_id = data['channel']
    user = data['user']

    web_client.chat_postMessage(
        channel=channel_id,
        text='<@{}> {}'.format(user, respond(content))
    )

print('Bot running ------------\n')

client = slack.RTMClient(
    token=bot_token,
    connect_method='rtm.start'
)
client.start()