import praw
from secret import client_id, client_secret, username, password

# log into reddit
reddit = praw.Reddit(client_id=client_id,
                     client_secret=client_secret,
                     username=username,
                     password=password,
                     user_agent='u/bot_username by u/your_username')