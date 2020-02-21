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
    return message


def main():
    while True:
        message = input(USER_TEMPLATE)
        response = respond(message)

        if "quit" in message.lower():
            print("Exiting, bye!")
            break
        print(BOT_TEMPLATE + response + "\n")


# code in this conditional will run if and only if the script is being run directly
# it won't run if we import our file as a module
if __name__ in "__main__":
    # start the main loop
    main()
