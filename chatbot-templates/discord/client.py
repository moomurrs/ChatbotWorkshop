import discord
import asyncio

## REMOVE THESE TWO LINES ##
import sys
sys.path.append('../..')

from BasicBot import respond

# client that connects with the Discord API
client = discord.Client()

@client.event
async def on_message(message):
    
    # if the bot was mentioned in the message, 
    # we want to process it
    if client.user in message.mentions:
        content = message.content.split(" ", 1)[1]
        print('{} sent a message: "{}"'.format(message.author.display_name, content))
        await message.channel.send('{} {}'.format(message.author.mention, respond(content)))

@client.event
async def on_ready():

    # this event fires when the bot is connected to Discord
    print('Logged in as {}\n---------------'.format(client.user.name))