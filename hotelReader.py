"""Python hotel data reader created for CS Club @ IU, Brady Anderson 2020"""
# module imports

from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import csv

# global configs
"""
+================================+
  hotel data reader
  Copyright CS Club @ IU, 2020
+================================+
"""

def hotelData(location, price, petFriendly, priceKeyword):
    # parameter default settings
    if(not priceKeyword):
      priceKeyword = "around"
    # fuzzy wuzzy matching of string values
    print(fuzz.token_sort_ratio("cowboys", "Dallas Cowboys"))

    # price handeling price and priceKeyword based

    # Price keyword -> around 

hotelData("a", "a", "", 0)