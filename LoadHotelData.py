import csv
import random
import string
import progressbar
import requests
from bs4 import BeautifulSoup

# +================================+
#  Hotel Data Webscraper
#  Copyright CS Club @ IU, 2020
# +================================+

headers = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
    "q": "requests+language:python",
}
url = "https://www.hilton.com/en/locations/"

page = requests.get(url, headers=headers)
soup = BeautifulSoup(page.text, "html.parser")

# get hotel data from around the world
hotels = soup.find_all("a", {"class": "sc-19wo0ah-6 dpWPln"})

# processing for all hotels
with open("hotels.csv", "w") as file:
    writer = csv.writer(file, delimiter=",")
    for hotel in progressbar.progressbar(hotels):
        identity = hotel["id"]
        href = hotel["href"]

        # scrape smaller pages
        subpage = requests.get(href, headers=headers)
        soup1 = BeautifulSoup(subpage.text, "html.parser")

        name = soup1.find_all("p", {"class": "hotel-card-dreamstyles__PropertyName-sc-1xoiocm-5 gUlGEE"})
        location = soup1.find_all("div", {"class": "hotel-card-dreamstyles__DistanceDiv-sc-1xoiocm-7 hpvmLI"})
        price = soup1.find_all("p", {"class": "hotel-card-dreamstyles__LeadRate-sc-1xoiocm-6 crEdua"})

        writer.writerow(["Name", "City", "State", "Price", "AllowsPets"])
        for i in range(len(name)):
            try:
                h_name = name[i].text
                h_city = location[i].text.split(", ")[0]
                h_state = location[i].text.split(", ")[1]
                h_price = int("".join([x for x in price[i].text if x in string.digits]))
                h_pets = random.choice((0, 1))
                writer.writerow([h_name, h_city, h_state, h_price, h_pets])
            except (IndexError, ValueError) as e:
                continue
