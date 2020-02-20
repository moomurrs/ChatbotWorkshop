## Slack bot setup

Before getting started: if you plan to run this bot in the same folder as your chatbot code, remove the two lines marked at the top of `run.py`.

1. Install requirements with `pip install -r requirements.txt`
1. Create a new Slack app: https://api.slack.com/apps?new_classic_app=1
    - Make sure it says (Classic)
1. Give the app a name and add it to your desired workspace
1. On the left, under "Features," go to "App Home".
1. Click "Add Legacy Bot User".
1. Fill out the display and full name.
1. Go back to the "Basic information" page.
1. Click "Install your app to your workspace".
1. Click "Allow".
1. Under "Features," click on the "OAuth & Permissions" page.
1. Copy the Bot User OAuth Access Token, then load it into `secret.py`. You could paste it directly into there, but if you're planning to put the source code online, you should add that file to your `.gitignore` or store it somewhere else like [in an environment variable](https://medium.com/@dtcarrot/we-should-be-using-environment-variables-to-secure-access-tokens-e2f057a6c0f0).
1. Run the bot with `python run.py`