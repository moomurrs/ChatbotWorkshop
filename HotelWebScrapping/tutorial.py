import requests
from urllib import urlopen
import time
from bs4 import BeautifulSoup

headers = {
    'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
    'q': 'requests+language:python'
}
url = "https://www.trivago.com/?themeId=101&iPathId=34812&sem_keyword=hotel%20website&sem_creativeid=393034754620&sem_matchtype=e&sem_network=g&sem_device=c&sem_placement=&sem_target=&sem_adposition=&sem_param1=&sem_param2=&sem_campaignid=99851526&sem_adgroupid=5212019886&sem_targetid=kwd-185941336&sem_location=9016568&cip=1061900383&gclid=EAIaIQobChMIivPG1InX5wIV0cDACh3oaQKyEAAYAyAAEgKQUPD_BwE"


page = requests.get(url, headers=headers)
soup = BeautifulSoup(page.text, "html.parser")

a = soup.find_next("div")

print(a)