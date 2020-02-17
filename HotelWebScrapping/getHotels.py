import requests
from urllib import urlopen
import time
from bs4 import BeautifulSoup
import csv

headers = {
    'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
    'q': 'requests+language:python'
}
url = "https://www.hilton.com/en/locations/"

page = requests.get(url, headers=headers)
soup = BeautifulSoup(page.text, "html.parser")

# get hotel data from around the world
hotels = soup.find_all("a", {"class":"sc-19wo0ah-6 dpWPln"})

# processing for all hotels
with open('hotelData2.csv', 'w') as file:
    writer = csv.writer(file, delimiter=',')
    for hotel in hotels:
        identity = hotel['id']
        href = hotel['href']

        # scrape smaller pages
        subpage = requests.get(href, headers = headers)
        soup1 = BeautifulSoup(subpage.text, "html.parser")

        name = soup1.find_all("p", {"class":"hotel-card-dreamstyles__PropertyName-sc-1xoiocm-5 gUlGEE"})
        location = soup1.find_all("div", {"class":"hotel-card-dreamstyles__DistanceDiv-sc-1xoiocm-7 hpvmLI"})
        price = soup1.find_all("p", {"class": "hotel-card-dreamstyles__LeadRate-sc-1xoiocm-6 crEdua"})

        writer.writerow(["Name", "Location", "Price per Night"])
        for i in range(len(name)):
            a = name[i].text.encode("utf8")
            b = location[i].text.encode("utf8")
            c = price[i].text.encode("utf8")
            writer.writerow([a, b, c])
                    


        
