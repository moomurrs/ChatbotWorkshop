"""Python Chatbot template created for CS Club @ IU, Wade Fletcher 2020"""

import random
import string

# global configs
USER_TEMPLATE = "[USER]: "  # prefix for user input messages
BOT_TEMPLATE = " [BOT]: "  # prefix for bot output messages (leading space is intentional, to make it line up nice)
STARTUP_MESSAGE = """
+================================+
  HotelBot
  Copyright CS Club @ IU, 2020
+================================+
"""  # message to be printed at the begining of script execution
LOCATION_KEYWORDS = ["Austin", "Houston"]
PRICE_UNIT_KEYWORDS = ["dollars"]

# global variables for use later
USER_INPUT = {"price": None, "location": None, "pet_friendly": None}


def respond(message):
    """Given a user's input message, perform appropriate decision-making to return an appropriate response."""

    # remove capitalization from input
    message = message.lower()
    # remove all punctuation from input
    message = "".join([m for m in message if m not in string.punctuation])
    # change all spaces to single spaces
    message = " ".join(message.split())

    message_words = message.split()
    for word in message_words:
        try:
            USER_INPUT["price"] = int(word)
        except ValueError:
            pass

    if USER_INPUT["price"]:
        bot_response = "I understood that you're looking for a hotel that costs around {} dollars.".format(USER_INPUT["price"])
    else:
        bot_response = "I didn't understand that."

    return bot_response


def main():
    """Main request-response loop"""

    # show the startup message
    print(STARTUP_MESSAGE)

    print(BOT_TEMPLATE + "Hey! I'm a chatbot to help you find a hotel! Could you tell me a little about what you're looking for?" + "\n")

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