## Discord bot setup
Before getting started: if you plan to run this bot in the same folder as your chatbot code, remove the two lines marked at the top of `client.py`.
1. Install requirements with `pip install -r requirements.txt`
1. Assuming you're already logged into discord, navigate to the [Discord Developer Portal](https://discordapp.com/developers/applications). 
1. Click the "New Application" button in the top-right. 
1. Go to the "Bot" tab and click "Add Bot".
1. Under the "Token" section, click "Copy". 
1. Paste the token somewhere safe, then load it in the `secret.py` file. You could paste it directly into there, but if you're planning to put the source code online, you should add that file to your `.gitignore` or store it somewhere else like [in an environment variable](https://medium.com/@dtcarrot/we-should-be-using-environment-variables-to-secure-access-tokens-e2f057a6c0f0).
1. Back on the Developer Portal, go to the "General Information" tab and copy your Client ID.
1. Go to the following URL:
    ```
    https://discordapp.com/oauth2/authorize?client_id=<CLIENT_ID_HERE>&scope=bot&permissions=2048
    ```
    and replace `<CLIENT_ID_HERE>` with the ID you copied. The `2048` represents only the "Send Messages" permission; you can add more by finding the "Bot Permissions" section on the Bot tab and checking them off to get a new number.
1. Select a server to add the bot to. Note that you have to have the "Manage Server" permission to add bots to any particular server.
1. Run the bot with `python run.py`
1. Send a message: 
    ```
    @BotNameHere hello there
    ```