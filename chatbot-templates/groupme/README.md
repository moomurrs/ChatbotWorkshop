## GroupMe bot setup

Before getting started: if you plan to run this bot in the same folder as your chatbot code, remove the two lines marked at the top of `run.py`.

1. Install requirements with `pip install -r requirements.txt`
1. Create a GroupMe account for your bot
1. As your bot, join a group.
    - Note: this bot in its current iteration is set up to work with one group, but you could extend the code for it to work with multiple.
1. Log into [GroupMe Developers](https://dev.groupme.com/) as your bot
1. On the right, click "Create Application".
1. Fill out the form info. For the callback url you can put something like example.com or `localhost`
1. Click "Save".
1. On the application's info page, copy the Access Token and load it into the `secret.py` file. You could paste it directly into there, but if you're planning to put the source code online, you should add that file to your `.gitignore` or store it somewhere else like [in an environment variable](https://medium.com/@dtcarrot/we-should-be-using-environment-variables-to-secure-access-tokens-e2f057a6c0f0).
1. In the same way, load/enter the name of the group that you'll be adding the bot to.
1. Run the bot with `python run.py`
1. Send a message:
    ```
    @BotNameHere hello there
    ```