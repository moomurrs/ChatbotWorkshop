"""Python Chatbot template created for CS Club @ IU, Wade Fletcher 2020"""

import random
import string
import HotelData

# global configs
USER_TEMPLATE = "[USER]: "  # prefix for user input messages
BOT_TEMPLATE = " [BOT]: "  # prefix for bot output messages (leading space is intentional, to make it line up nice)
STARTUP_MESSAGE = """
+================================+
  HotelBot
  Copyright CS Club @ IU, 2020
+================================+
"""  # message to be printed at the begining of script execution


# global variables for use later
USER_INPUT = {"price": None, "city": None, "state": None, "pet_friendly": None}


def respond(message):
    """Given a user's input message, perform appropriate decision-making to return an appropriate response."""

    # remove capitalization from input
    message = message.lower()
    # remove all punctuation from input
    message = "".join([m for m in message if m not in string.punctuation])
    # change all spaces to single spaces
    message = " ".join(message.split())

    # this is the bag-of-words we discussed earlier
    message_words = message.split()

    # extract what data we can from our bag of words, matching words to our known words
    for word in message_words:
        try:
            USER_INPUT["price"] = int(word)
        except ValueError:
            pass

        if word in HotelData.CITY_NAMES:
            USER_INPUT["city"] = word

        if word in HotelData.STATE_NAMES:
            USER_INPUT["state"] = word

    # if we're missing data, let's ask the user for it
    if USER_INPUT["price"] is None:
        return "What price point are you looking for?"
    if USER_INPUT["city"] is None:
        return "In what city are you looking for a hotel?"
    if USER_INPUT["state"] is None:
        return "In what state are you looking for a hotel?"

    results = HotelData.findHotels(city=USER_INPUT["city"], state=USER_INPUT["state"], price=USER_INPUT["price"])

    bot_response = "I found {} hotels matching your criteria!".format(len(results))
    if len(results) > 0:
        bot_response += " I'd recommend the {name}, in {city}, {state} which costs ${price}/night.".format(
            name=results[0]["Name"], city=results[0]["City"], state=results[0]["State"], price=results[0]["Price"]
        )

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
