## Twitter bot setup
Before getting started: if you plan to run this bot in the same folder as your chatbot code, remove the two lines marked at the top of `stream_listener.py`.
1. Install requirements with `pip install -r requirements.txt`
1. Go to the [Twitter Developer](https://developer.twitter.com/) website.
1. In the upper-right corner, click "Apply".
1. Click "Apply for access".
    - If you haven't already, you'll have to create an account. This account is the one the bot will be using to tweet. It needs to have a valid email address to submit an application for a developer account. You can use your IU email or a throwaway email address from a site like https://temp-mail.org/en/
1. On the use case page, select "Making a bot".
1. Fill out your personal information on the next page.
1. On the next page, check off the requirements for your account. You'll probably only need to select the one that says "Will your app use Tweet, Retweet, like, follow, or Direct Message functionality?"
    - What you type into the box doesn't really matter, as long as it has something to do with the bot.
1. Review the application info and submit.
1. Check your inbox and click the "Confirm your email" link.
1. After the application has been approved, go back to the Twitter Developer site, and click the dropdown with your username. Click on "Apps".
1. Click "Create an app"
1. Fill out the form.
    - You only need to fill in the required fields. For Website URL, you can put a real website or just some fake web address. 
1. Go to the "keys and tokens" tab
1. Grab the keys from the "Consumer API keys" section and load them into `secret.py`. You could paste them directly into there, but if you're planning to put the source code online, you should add that file to your `.gitignore` or store them somewhere else like [in environment variables](https://medium.com/@dtcarrot/we-should-be-using-environment-variables-to-secure-access-tokens-e2f057a6c0f0).
1. Under "Access token & access token secret", click "Create" and repeat the previous step.
    - You can also store your bot's handle in that file if you want to keep it hidden in your source code.
1. Run the bot with `python run.py`
1. Tweet a message: 
    ```
    @BotHandle hello there
    ```