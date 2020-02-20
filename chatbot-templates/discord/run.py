import discord
from client import client
from secret import bot_token

if __name__ == '__main__':

    # start the bot
    client.run(bot_token)