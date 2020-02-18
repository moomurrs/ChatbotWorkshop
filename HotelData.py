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
CITY_NAMES = [x.lower() for x in list(df["City"])]
STATE_NAMES = [x.lower() for x in list(df["State"])]
PRICE = [x for x in list(df["Price"])]

# all are set to None as default because we will likely have incomplete data
# you'll need to check "if state:", "if price:" etc. before using each one
def findHotels(city=None, state=None, price=None, petFriendly=None, price_variance=30):
    # add pandas filtering -> super effective
    # clean parameters to be accepted w/ fuzzywuzzy
    s = process.extract(state, STATE_NAMES, limit=1)
    p = []
    h = []
    pf = []
    c = []
    # iterate through all dataframes to get relevant data
    for i, j in df.iterrows(): 
      # get hotels in state and perform price matching - keep track of hotels and pet friendly
      if(j[2] == s[0][0].upper()):
        p.append(str(j[3]))
        h.append(j[0])
        pf.append(j[4])
        c.append(j[1])
    # check other preferences of relevant data
    max = price + price_variance
    min = price - price_variance
    bestOptions = []
    priceOptions = []
    petOptions = []
    # process relevant data
    for i in range(len(h)):
      if(int(p[i]) < max and int(p[i]) > min and pf[i] == petFriendly):      # both conditions satisfied!
        bestOptions.append({"hotel": h[i], "city":c[i], "price": p[i], "pets-allowed":pf[i]})
      elif(int(p[i]) > min and int(p[i]) < max):                # only good price
        priceOptions.append({"hotel": h[i], "city":c[i], "price": p[i], "pets-allowed":pf[i]})
      elif(pf[i] == petFriendly):      # only petfriendly
        petOptions.append({"hotel": h[i], "city":c[i], "price": p[i], "pets-allowed":pf[i]})
    return bestOptions, priceOptions, petOptions
        
if __name__ in "__main__":
    findHotels("AZ", "Ri", 100, 0)

