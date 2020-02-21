"""Python Chatbot template created for CS Club @ IU, Wade Fletcher 2020"""

import random
import string

# global configs
USER_TEMPLATE = "[USER]: "  # prefix for user input messages
BOT_TEMPLATE = " [BOT]: "  # prefix for bot output messages (leading space is intentional, to make it line up nice)
STARTUP_MESSAGE = """
+================================+
  BasicBot
  Copyright CS Club @ IU, 2020
+================================+
"""  # message to be printed at the begining of script execution


def respond(message):
    """Given a user's input message, perform appropriate decision-making to return an appropriate response."""

    message = message.lower()
    # filter out punctuation
    message = "".join([ m for m in message if m not in string.punctuation])
    # divide each word by spaces
    message = " ".join(message.split())

    # ignore the fmt comments, black formatter doesn't like the way i structured this dict
    # fmt: off
    responses = {
        "hello there": ["General Kenobi!"],
        "you killed my father": ['No. I am your father.'],
        # we're using * as a wildcard, so these are the responses for when no others match.
        "*": ["I'm sorry, I'm afraid I don't quite understand."]
    }
    # fmt: on

    if message in responses:
        bot_response = random.choice(responses[message])
    else:
        bot_response = random.choice(responses["*"])

    return bot_response


def main():
    """Main request-response loop"""

    # show the startup message
    print(STARTUP_MESSAGE)

    # start a (kinda) infinite loop, so we can carry on a conversation
    while True:
        # ask the user for input, using the prompt defined in USER_TEMPLATE
        message = input(USER_TEMPLATE)

        # exit the loop (and therefore the program) when the message 'quit' is sent
        # (this is why our loop is only (kinda) infinite)
        if message == "quit":
            print("Exiting, bye!")
            break

        # given a user's input message, pass it to the bot response() function and save the result
        response = respond(message)

        # output the bot's response, prefixed by BOT_TEMPLATE and followed by a new line (\n)
        print(BOT_TEMPLATE + response + "\n")


# code in this conditional will run if and only if the script is being run directly
# it won't run if we import our file as a module
if __name__ in "__main__":
    # start the main loop
    main()
