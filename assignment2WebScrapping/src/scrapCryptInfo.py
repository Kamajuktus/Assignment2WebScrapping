import requests
from bs4 import BeautifulSoup

class CryptInfoScrapper:
    url = "https://coinmarketcap.com"
    content = requests.get(url).text
    soup = BeautifulSoup(content, features="lxml")

    table = soup.find("table", attrs={"class" : ["h7vnx2-2", "czTsgW", "cmc-table"]})
    global tr_list
    tr_list = table.tbody.find_all("tr")

    @staticmethod
    def scrapCryptInfo(cryptoName):
        for x in range(100):
            for a in tr_list[x].find_all("td"):
                if  tr_list[x].find_all("td")[2].text.lower().find(cryptoName.lower()) != -1:
                    print(a.text)