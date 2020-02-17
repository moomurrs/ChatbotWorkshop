"""Python hotel data reader created for CS Club @ IU, Brady Anderson 2020"""
# module imports

import csv

import pandas as pd

from fuzzywuzzy import fuzz, process

# global configs
"""
+================================+
  hotel data reader
  Copyright CS Club @ IU, 2020
+================================+
"""

df = pd.read_csv("hotels.csv")
CITY_NAMES = list(df["City"])
STATE_NAMES = list(df["State"])


# all are set to None as default because we will likely have incomplete data
# you'll need to check "if state:", "if price:" etc. before using each one
def findHotels(city=None, state=None, price=None, petFriendly=None, price_variance=30):
    # fuzzy wuzzy matching of string values
    print(fuzz.token_sort_ratio("cowboys", "Dallas Cowboys"))

    # price handeling price and priceKeyword based

    # Price keyword -> around


if __name__ in "__main__":
    findHotels("a", "a", "", 0)

