## Reddit bot setup
Before getting started: if you plan to run this bot in the same folder as your chatbot code, remove the two lines marked at the top of `run.py`.
1. Install requirements with `pip install -r requirements.txt`
1. Create a [Reddit](https://reddit.com) account for your bot
1. Go to your [authorized applications](https://old.reddit.com/prefs/apps/)
1. Click "create another app" at the bottom.
1. Give the app a name, select "script," and enter any address (like example.com) into the "redirect uri" section.
1. After creation, copy the client ID under "personal use script" and load it into `secrets.py`. You could paste it directly into there, but if you're planning to put the source code online, you should add that file to your `.gitignore` or store it somewhere else like [in an environment variable](https://medium.com/@dtcarrot/we-should-be-using-environment-variables-to-secure-access-tokens-e2f057a6c0f0).
1. Do the same with the "secret" field in your app's information section as well as the username and password for the bot's account.
1. Run the bot with `python run.py`
1. Comment on a post somewhere and tag your bot:
    ```
    u/bot-name hello there
    ```